from abc import ABC, abstractmethod

import pyrogram
from loguru import logger

from app.settings import Settings


class BaseCommand(ABC):
    """Базовая команда pyrogram"""

    def __init__(self, settings: Settings):
        self._settings = settings

    @property
    def full_text(self) -> str:
        return f"{self.prefix}{self.text}"

    @property
    @abstractmethod
    def description(self) -> str:
        """Описание команды"""
        ...

    @property
    @abstractmethod
    def filters(self) -> pyrogram.filters.Filter:
        """Фильтры команды"""
        ...

    @property
    @abstractmethod
    def prefix(self) -> str:
        """Префикс команды"""
        ...

    @property
    @abstractmethod
    def text(self) -> str:
        """Текст команды"""

    def handle(self, client: pyrogram.client.Client, message: pyrogram.types.Message) -> None:
        """Обработчик команды"""
        self.log(f"start, text={message.text}, {message=}")
        self.execute(client=client, message=message)
        self.log(f"finish")

    @abstractmethod
    def execute(self, client: pyrogram.client.Client, message: pyrogram.types.Message) -> None:
        """Выполнение действий по команде"""
        ...

    def log(self, message: str) -> None:
        logger.debug(f"{self.__class__.__name__}, {message}")


class BaseDotCommand(BaseCommand, ABC):
    """Базовая команда начинающаяся с точки"""

    @property
    def prefix(self) -> str:
        return "."
