from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///:memory:"
    db_echo: bool = True

    usos_api_key: str
    usos_api_secret: str

    session_secret: str

    class Config:
        env_prefix = ""
        env_file = ".env"


settings = Settings()  # type: ignore
