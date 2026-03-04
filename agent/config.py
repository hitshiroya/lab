import os
from dotenv import load_dotenv

load_dotenv()


class LLMProvider:
    GROQ = "groq"
    OLLAMA = "ollama"


class Config:
    # ── Provider ──────────────────────────────────────────────────────────────
    PROVIDER: str = os.getenv("LLM_PROVIDER", LLMProvider.GROQ).lower()

    # ── Groq ──────────────────────────────────────────────────────────────────
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

    # ── Ollama ────────────────────────────────────────────────────────────────
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3")

    # ── Agent ─────────────────────────────────────────────────────────────────
    WORKSPACE: str = os.getcwd()
    AGENT_NAME: str = "Smarty"

    @classmethod
    def active_model(cls) -> str:
        if cls.PROVIDER == LLMProvider.GROQ:
            return cls.GROQ_MODEL
        return cls.OLLAMA_MODEL

    @classmethod
    def validate(cls) -> tuple[bool, str]:
        if cls.PROVIDER == LLMProvider.GROQ:
            if not cls.GROQ_API_KEY:
                return False, "GROQ_API_KEY is not set. Add it to your .env file."
        elif cls.PROVIDER == LLMProvider.OLLAMA:
            if not cls.OLLAMA_BASE_URL:
                return False, "OLLAMA_BASE_URL is not set."
        else:
            return False, f"Unknown LLM_PROVIDER '{cls.PROVIDER}'. Use 'groq' or 'ollama'."
        return True, ""
