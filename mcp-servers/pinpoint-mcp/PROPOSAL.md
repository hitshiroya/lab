# pinpoint-mcp — Project Proposal

## What It Is

An MCP server that lives inside Cursor and fixes the biggest failure point in AI-generated tests: wrong selectors.

Instead of letting Cursor guess at selectors (and hallucinate them), `tc-generator-mcp` scans the real live page first and hands Cursor ground truth — verified selectors, detected user flows, and plain English test case definitions. Cursor then writes the actual test code using only what the tool provided.

---

## The Problem It Solves

When Cursor (or any LLM) generates Playwright tests without real page data, it invents selectors based on training patterns. Those selectors are frequently wrong, brittle, or simply do not exist on the target page. The developer then spends more time debugging selectors than they saved using AI.


---

## The Flow

```
Developer prompt in Cursor
"give me supportive data to generate test cases for https://www.saucedemo.com/"
        ↓
Cursor calls pinpoint-mcp tools
        ↓
MCP server launches headless browser → scans the live page
        ↓
Extracts interactive elements → scores selectors → dry runs each selector
        ↓
Detects user flows → generates plain English test case definitions
        ↓
Returns structured payload to Cursor
        ↓
Cursor writes Playwright test code using only the provided selectors
```

No hallucination possible — Cursor is bounded by the verified payload.

---

## MCP Tools Exposed

### Tool 1: `analyze_page(url)`

The primary tool. Does the full scan and returns the complete structured payload.

**Internally it:**
1. Visits the page and waits for JavaScript frameworks to settle (network idle, not just DOM load)
2. Extracts all interactable elements (inputs, buttons, links, forms, navigation)
3. Scores each element's selectors by reliability
4. Dry runs each primary selector against the live DOM to confirm it resolves
5. Falls back to secondary selector if primary fails
6. Detects user flows by pattern matching on page structure
7. Generates plain English test case definitions per flow
8. Returns the complete verified payload

---

### Tool 2: `validate_selector(url, selector)`

A lightweight utility tool. Takes a URL and a selector string, confirms it resolves to exactly one element on the live page, and returns what it found.

Cursor calls this optionally when it wants to verify a selector before writing a test. Internally reuses the same validation logic as `analyze_page`.

---

## Internal Data Flow

```
scanner.py    →  visit page, extract raw interactive elements
      ↓
scorer.py     →  score and rank selectors per element
      ↓
validator.py  →  dry run each selector against live DOM, flag failures
      ↓
flows.py      →  pattern-match user flows from validated elements
      ↓
models.py     →  assemble and return clean structured payload
```

Each layer has one job. Nothing bleeds into another.

---

## Selector Scoring — Priority Cascade

Selectors are scored and ranked in this order. Higher = more stable:

| Priority | Selector Type | Reason |
|---|---|---|
| 1 | `data-testid`, `data-test`, `data-cy` | Developer expressed intent |
| 2 | `aria-label`, `role` + accessible name | Semantic, survives visual redesigns |
| 3 | `id` (non-dynamic) | Stable if not auto-generated |
| 4 | `name` attribute | Reliable for form fields |
| 5 | `placeholder` text | Decent for inputs |
| 6 | Meaningful CSS class | Down-scored if utility classes (Tailwind, Bootstrap) detected |
| 7 | Text content | Fragile but sometimes only option |
| 8 | XPath / positional | Last resort |

**Dynamic ID detection:** If an `id` contains more than 2 digits or matches UUID/hash patterns, it is treated as unstable and down-scored.

Each element in the payload gets a `primary` selector, a `fallback` selector, and a `reliability_score` (0–100).

---

## Selector Dry Run

After scoring, every primary selector is verified against the live DOM in the same browser context. The check confirms:

- Does it resolve to at least one element?
- Does it resolve to exactly one element? (ambiguous = problem)
- Is it the same element originally extracted?

**If primary fails:** try fallback selector.  
**If fallback also fails:** element is included in payload but marked `verified: false`.

Elements are never silently dropped. Cursor sees everything, including unreliable ones — flagged clearly.

---

## Flow Detection — Heuristics

Flows are detected by pattern matching on page structure, not ML.

| Pattern Detected | Flow Named |
|---|---|
| Password field present | Login candidate |
| Multiple text inputs + password field | Registration candidate |
| Single input + button with search-related text/aria | Search flow |
| `nav` element with multiple links | Navigation flow |
| Submit button near price/payment elements | Checkout candidate |

Each detected flow outputs:
- A `confidence` score (0–1)
- Ordered steps with element references and plain English descriptions
- Plain English test case definitions (what to test, not how to code it)

---

## Output Payload Shape

```json
{
  "page": {
    "url": "https://access.redhat.com",
    "title": "Red Hat Customer Portal",
    "framework_hint": "react"
  },
  "elements": [
    {
      "id": "el_01",
      "tag": "button",
      "role": "button",
      "text": "Log In",
      "type": "button",
      "selectors": {
        "primary": "[data-testid='login-btn']",
        "fallback": "[aria-label='Log In']",
        "score": 95
      },
      "verified": true
    }
  ],
  "flows": [
    {
      "name": "login",
      "confidence": 0.92,
      "test_cases": [
        "Verify user can log in with valid credentials",
        "Verify error message appears on invalid password",
        "Verify login button is visible and clickable on page load"
      ],
      "steps": [
        { "action": "fill",  "element_id": "el_02", "description": "Enter email address" },
        { "action": "fill",  "element_id": "el_03", "description": "Enter password" },
        { "action": "click", "element_id": "el_01", "description": "Click Log In button" }
      ]
    }
  ]
}
```

---

## Project Structure

```
test-pilot-mcp/
├── server.py              # MCP server entry point, tool definitions
├── browser/
│   └── scanner.py         # Playwright logic — visit, extract, close
├── analyzer/
│   ├── scorer.py          # Selector scoring by priority cascade
│   ├── validator.py       # Dry run — confirm selectors resolve on live DOM
│   └── flows.py           # Flow detection heuristics
├── schema/
│   └── models.py          # Pydantic models for the output payload
├── pyproject.toml
└── README.md
```

---

## Browser Lifecycle

One browser instance per `analyze_page` call. One isolated context. Close after done.

No pooling, no reuse across calls. Simple and safe. Optimize later if scan speed becomes a pain point.

---

## Build Order

| Step | What Gets Built | Why This Order |
|---|---|---|
| 1 | `schema/models.py` | Define the contract first. Everything else builds toward this. |
| 2 | `browser/scanner.py` | Core data collection. Independently testable. |
| 3 | `analyzer/scorer.py` | Works on scanner output. No browser needed to test. |
| 4 | `analyzer/validator.py` | Needs browser + scored elements. |
| 5 | `analyzer/flows.py` | Works on validated elements. |
| 6 | `server.py` | Wire everything into MCP tools last. |

---

## Out of Scope for MVP

- Authentication / session handling
- Post-interaction state capture (modals, dropdowns after click)
- Multi-page crawling
- Caching / TTL
- Context window optimization
- Framework-specific selector strategies

These are known future concerns. They will be addressed if and when this proves useful in practice.

---

## Success Criteria for MVP

A developer can:
1. Link `pinpoint-mcp` to Cursor like any other MCP server
2. Ask Cursor to generate tests for any public URL
3. Receive a Playwright test file that uses real, verified selectors from the live page
4. Run that test file without having to manually fix broken selectors
