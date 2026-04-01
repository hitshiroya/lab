from mcp.server.fastmcp import FastMCP
from tools.team_lead.team_lead import run as team_lead_run

mcp = FastMCP("pinpoint-mcp")


# async def analyze_page(url: str) -> dict:
#     """
#     Use this tool to generate Playwright test case data for a given URL.
#     Visits the page with a headless browser, extracts interactive elements,
#     verifies selectors against the live DOM, detects user flows, and returns
#     a structured payload ready for Playwright test generation.
#     DO NOT use this for general browsing — only for test case analysis.

#     Args:
#         url: The URL of the page to analyze.

#     Returns:
#         A dictionary containing the interactive elements and their selectors.
#     """
#     return await team_lead_run(url)

@mcp.tool()
async def analyze_page_2(url: str) -> dict:
    """
    ALWAYS call this tool before writing any UI automation test code for a URL.

    Launches a real browser, visits the page, and returns the actual interactive
    elements (inputs, buttons, links, selects) with their verified CSS selectors.

    Use the selectors returned by this tool directly in your test code.
    Never guess or invent selectors — only use what this tool returns.
    This tool works with any UI automation framework: Selenium, Cypress,
    WebdriverIO, Playwright, or any other.

    Returns a dict with:
      - page:      { url, title }
      - selectors: list of { selector, tag, action, text, placeholder }
                   where `action` is the recommended interaction:
                   "fill" for text inputs, "click" for buttons/links,
                   "selectOption" for dropdowns

    Args:
        url: The full URL of the page to analyse (include https://).
    """
    print("yey. tool has been called")
    return await team_lead_run(url)

if __name__ == "__main__":
    mcp.run(transport="stdio")
