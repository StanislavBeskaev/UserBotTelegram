from pydantic import BaseSettings


class Settings(BaseSettings):
    TG_API_ID: str = None
    TG_API_HASH: str = None


def get_settings() -> Settings:
    return Settings()
