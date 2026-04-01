import re
from playwright.async_api import async_playwright

ELEMENT_CAP      = 20
MAX_RETRIES      = 2
FAILURE_THRESHOLD = 0.75   # retry the whole scan if > 75 % of selectors fail validation


async def scan_page(url: str) -> dict:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page    = await browser.new_page()
        await page.goto(url, timeout=15_000, wait_until="domcontentloaded")

        page_meta = {
            "url":   url,
            "title": await page.title(),
        }

        selectors:   list[dict] = []
        retry_queue: list[dict] = []
        stats:       dict       = {}

        for attempt in range(MAX_RETRIES + 1):
            if attempt > 0:
                # give the page a moment to settle before re-scanning
                await page.wait_for_timeout(1500)
                print(f"[scanner] retrying (attempt {attempt + 1})")

            raw       = await _extract_id_selectors(page)
            validated = await _validate_selectors(page, raw)

            passed = [s for s in validated if     s["valid"]]
            failed = [s for s in validated if not s["valid"]]
            total  = len(validated)
            ratio  = len(failed) / total if total else 0.0

            print(
                f"[scanner] attempt={attempt + 1}  "
                f"total={total}  passed={len(passed)}  "
                f"failed={len(failed)}  failure_ratio={ratio:.0%}"
            )

            # if too many selectors failed AND we still have retries left, go again
            if ratio > FAILURE_THRESHOLD and attempt < MAX_RETRIES:
                print(f"[scanner] failure ratio {ratio:.0%} exceeds threshold — queuing and retrying")
                retry_queue = failed
                continue

            selectors   = passed
            retry_queue = failed
            stats = {
                "attempt":       attempt + 1,
                "total":         total,
                "passed":        len(passed),
                "failed":        len(failed),
                "failure_ratio": round(ratio, 2),
            }
            break

        await browser.close()

    return {
        "page":        page_meta,
        "selectors":   selectors,
        "retry_queue": retry_queue,
        "stats":       stats,
    }


# ---------------------------------------------------------------------------
# Extractor — id-based selectors only
# ---------------------------------------------------------------------------

INTERACTIVE_TAGS = "a[id], button[id], input[id], select[id], textarea[id]"

_CLICK_INPUT_TYPES = {"submit", "button", "reset", "checkbox", "radio", "file"}


def _action_for(tag: str, input_type: str | None) -> str:
    """Return the Playwright method Cursor should use for this element."""
    if tag == "select":
        return "selectOption"
    if tag in ("a", "button"):
        return "click"
    if tag == "input" and input_type in _CLICK_INPUT_TYPES:
        return "click"
    return "fill"   # input[text/email/password/search/…] and textarea

# Patterns that indicate an auto-generated / random ID — not stable selectors
_NOISE_PATTERNS = re.compile(
    r"""
    # UUID (with or without braces)
    [0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}
    # pure number or starts with a digit
    | ^[0-9]
    # contains a dot (invalid in CSS without escaping, usually random)
    | \.
    # framework-generated prefixes
    | ^(ember|react|ng-|vue|radix-|:r)
    # long hex / hash strings (>= 8 hex chars in a row)
    | [0-9a-f]{8,}
    # looks like an internal counter: word + digits only, e.g. item3849
    | ^[a-z]+\d{4,}$
    # very short (single char) or very long (likely generated)
    """,
    re.VERBOSE | re.IGNORECASE,
)


def _is_noisy_id(el_id: str) -> bool:
    """Return True if the id looks auto-generated and should be skipped."""
    if not el_id or len(el_id) > 60:
        return True
    if _NOISE_PATTERNS.search(el_id):
        return True
    # catch random alphanumeric suffixes like "pfe-detail-toggle-xjnb6p954-"
    # any segment (split on - or _) that mixes letters AND digits and is 6+ chars
    segments = re.split(r"[-_]", el_id)
    if any(
        len(s) >= 6 and re.search(r"[a-z]", s, re.I) and re.search(r"[0-9]", s)
        for s in segments
    ):
        return True
    return False


async def _extract_id_selectors(page) -> list[dict]:
    """
    Collect up to ELEMENT_CAP interactive elements (a, button, input, select,
    textarea) that have an id attribute. Ignores structural/non-interactive tags.
    Returns a flat list of raw (not yet validated) selector dicts.
    """
    handles  = await page.query_selector_all(INTERACTIVE_TAGS)
    results  = []
    seen_ids: set[str] = set()

    for handle in handles:
        if len(results) >= ELEMENT_CAP:
            break
        try:
            el_id = await handle.get_attribute("id")
            if not el_id or el_id in seen_ids or _is_noisy_id(el_id):
                continue
            seen_ids.add(el_id)

            tag  = await handle.evaluate("el => el.tagName.toLowerCase()")
            text = (await handle.text_content() or "").strip()[:80] or None

            placeholder = await handle.get_attribute("placeholder") or None
            input_type  = await handle.get_attribute("type") or None

            results.append({
                "selector":    f"#{el_id}",
                "tag":         tag,
                "action":      _action_for(tag, input_type),
                "text":        text,
                "placeholder": placeholder,
            })
        except Exception:
            continue

    return results


# ---------------------------------------------------------------------------
# Validator
# ---------------------------------------------------------------------------

async def _validate_selectors(page, selectors: list[dict]) -> list[dict]:
    """
    Validate every selector.  A selector is valid when it:
      1. resolves to exactly one element in the DOM   (unique)
      2. that element is visible to the user          (not hidden)
    Failed selectors are marked valid=False and pushed to the retry queue
    by the caller.
    """
    results = []
    for entry in selectors:
        valid, reason = await _validate_one(page, entry["selector"])
        results.append({**entry, "valid": valid, "fail_reason": reason})
    return results


async def _validate_one(page, selector: str) -> tuple[bool, str | None]:
    try:
        elements = await page.query_selector_all(selector)

        if len(elements) == 0:
            return False, "not_found"

        if len(elements) > 2:
            return False, "not_unique"

        visible = await elements[0].is_visible()
        if not visible:
            return False, "not_visible"

        return True, None

    except Exception as exc:
        return False, str(exc)
