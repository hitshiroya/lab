from pydantic import BaseModel


class PageInfo(BaseModel):
    url: str
    title: str
    framework_hint: str | None = None
    wait_strategy: str = "domcontentloaded"


class SelectorInfo(BaseModel):
    primary: str
    fallback: str | None = None
    score: int  # 0-100


class Element(BaseModel):
    id: str                   # e.g. "el_01"
    tag: str                  # e.g. "button", "input", "a"
    role: str | None = None   # ARIA role
    text: str | None = None   # visible text content
    type: str | None = None   # input type, button type, etc.
    selectors: SelectorInfo
    verified: bool = False    # True if primary selector resolved on live DOM


class FlowStep(BaseModel):
    action: str        # "fill", "click", "select", "navigate"
    element_id: str    # references Element.id
    description: str   # plain English e.g. "Enter email address"


class Flow(BaseModel):
    name: str                    # e.g. "login", "search", "registration"
    confidence: float            # 0.0 - 1.0
    test_cases: list[str]        # plain English test definitions
    steps: list[FlowStep]


class AnalysisResult(BaseModel):
    page: PageInfo
    elements: list[Element]
    flows: list[Flow]
