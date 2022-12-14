from typing import Type

import pyrogram
from loguru import logger

from app.commands.base_command import BaseCommand
from app.settings import Settings


class CommandAlreadyExistError(Exception):
    """Ошибка уже существующей команды"""

    pass


class CommandManager:
    """Менеджер для управления командами"""

    def __init__(self, app: pyrogram.client, settings: Settings):
        self._app = app
        self._settings = settings
        self._commands = []

    def register_command(self, command: Type[BaseCommand]):
        """Регистрация команды в приложении"""
        command_instance = command(settings=self._settings)
        command_full_text = f"{command_instance.prefix}{command_instance.text}"
        self._check_command_exist(command_full_text)
        self._commands.append(command_full_text)

        self._app.add_handler(
            pyrogram.handlers.MessageHandler(callback=command_instance.handle, filters=command_instance.filters)
        )
        logger.info(f"Добавлена команда {command_full_text}: {command_instance.description}")

    def _check_command_exist(self, command_full_text: str) -> None:
        if command_full_text in self._commands:
            raise CommandAlreadyExistError(f"Команда '{command_full_text}' уже есть!")
