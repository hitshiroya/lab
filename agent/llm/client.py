from typing import Iterator
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage

from config import Config, LLMProvider


SYSTEM_PROMPT = """You are Smarty, a sharp and friendly AI coding assistant.
You help developers build projects, write test cases, and debug issues.
You are running inside the developer's terminal — keep responses focused, clear, and practical.
When writing code, always use the correct language and framework for the project.
Never be verbose. Be like a senior dev who respects the other person's time."""


def get_llm() -> BaseChatModel:
    if Config.PROVIDER == LLMProvider.GROQ:
        from langchain_groq import ChatGroq
        return ChatGroq(
            api_key=Config.GROQ_API_KEY,
            model=Config.GROQ_MODEL,
            streaming=True,
        )

    from langchain_ollama import ChatOllama
    return ChatOllama(
        base_url=Config.OLLAMA_BASE_URL,
        model=Config.OLLAMA_MODEL,
    )


def stream_response(user_input: str, history: list[dict]) -> Iterator[str]:
    llm = get_llm()

    messages = [SystemMessage(content=SYSTEM_PROMPT)]

    for turn in history:
        if turn["role"] == "user":
            messages.append(HumanMessage(content=turn["content"]))
        else:
            from langchain_core.messages import AIMessage
            messages.append(AIMessage(content=turn["content"]))

    messages.append(HumanMessage(content=user_input))

    for chunk in llm.stream(messages):
        if chunk.content:
            yield chunk.content
