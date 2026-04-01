from tools.scanner.scanner import scan_page


async def run(url: str) -> dict:
    """
    Orchestrates the analysis pipeline and shapes the final output for Cursor.
    Returns only clean, verified selectors — no pipeline internals.
    """
    print(f"[team_lead] Scanning {url}")
    result = await scan_page(url)

    stats = result["stats"]
    print(
        f"[team_lead] Scanner done — "
        f"passed={stats['passed']}  failed={stats['failed']}  "
        f"failure_ratio={stats['failure_ratio']:.0%}  attempts={stats['attempt']}"
    )

    if not result["selectors"]:
        print("[team_lead] No valid selectors found.")

    # Strip validation internals — Cursor only needs selector + action metadata
    clean_selectors = [
        {k: v for k, v in el.items() if k not in ("valid", "fail_reason")}
        for el in result["selectors"]
    ]

    return {
        "page":      result["page"],
        "selectors": clean_selectors,
    }
