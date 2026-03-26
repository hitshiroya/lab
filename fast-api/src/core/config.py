from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    mcp_base_url: str = "http://localhost:8000/api/v1"

    class Config:
        env_file = ".env"


settings = Settings()
