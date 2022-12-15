from loguru import logger
from pydantic import BaseSettings


class Settings(BaseSettings):
    TG_API_ID: str = None
    TG_API_HASH: str = None
    TYPING_SYMBOL: str = "▒"
    TYPING_PAUSE_INTERVAL: float = 0.05
    TYPING_SYMBOL_INTERVAL: float = 0.02
    FLOOD_WAIT_INTERVAL: float = 0.05
    JOKE_CHOICE_INTERVAL: float = 1.0


def get_settings() -> Settings:
    settings = Settings()
    _check_settings(settings)

    return Settings()


def _check_settings(settings: Settings) -> None:
    logger.debug("Проверяем настройки")

    if not settings.TG_API_ID:
        print("Укажите api_id в переменной окружения TG_API_ID")
        exit(1)
    logger.debug("TG_API_ID указан")

    if not settings.TG_API_HASH:
        print("Укажите api_hash в переменной окружения TG_API_HASH")
        exit(1)
    logger.debug("TG_API_HASH указан")

    logger.debug("Настройки заданы корректно")
