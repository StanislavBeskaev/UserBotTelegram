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
        self._check_command_exist(command_instance)
        self._commands.append(command_instance.full_text)

        self._app.add_handler(
            pyrogram.handlers.MessageHandler(callback=command_instance.handle, filters=command_instance.filters)
        )
        logger.info(f"Добавлена команда {command_instance.full_text}: {command_instance.description}")

    def _check_command_exist(self, command_instance: BaseCommand) -> None:
        if command_instance.full_text in self._commands:
            raise CommandAlreadyExistError(f"Команда '{command_instance.full_text}' уже есть!")
