# pinpoint-mcp

> Pinpoint real CSS selectors on any live page — stop AI from hallucinating selectors in UI automation tests.

## What it does

When Cursor (or any AI) writes UI automation tests, it guesses selectors from training data. Those guesses are often wrong.

**pinpoint-mcp** launches a real browser, visits the page, extracts only the interactive elements (`input`, `button`, `a`, `select`, `textarea`) that have stable, human-written IDs, validates each selector is unique and visible, and returns the ground truth to Cursor — so the generated test code uses selectors that actually exist.

## How it works

```
Cursor: "write a test for https://example.com"
    ↓
pinpoint-mcp called automatically
    ↓
Headless browser visits the page
    ↓
Extracts interactive elements with clean id attributes
    ↓
Validates each selector (unique + visible)
    ↓
Returns verified selectors to Cursor
    ↓
Cursor writes test code with real selectors
```

## Tools

### `analyze_page_2(url)`

Visits the URL and returns verified interactive selectors.

**Returns:**
```json
{
  "page": { "url": "...", "title": "..." },
  "selectors": [
    { "selector": "#user-name",    "tag": "input",  "action": "fill",  "text": null, "placeholder": "Username" },
    { "selector": "#password",     "tag": "input",  "action": "fill",  "text": null, "placeholder": "Password" },
    { "selector": "#login-button", "tag": "button", "action": "click", "text": "Login", "placeholder": null }
  ]
}
```

## Setup

```bash
cd mcp-servers/pinpoint-mcp
uv sync
playwright install chromium
```

Add to `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "pinpoint-mcp": {
      "command": "/path/to/.venv/bin/python",
      "args": ["/path/to/src/server.py"],
      "cwd": "/path/to/pinpoint-mcp"
    }
  }
}
```
