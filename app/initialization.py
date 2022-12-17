import importlib
import inspect
import pkgutil
from typing import Type

import pyrogram
from loguru import logger

from app import commands
from app.commands.base_command import BaseCommand
from app.settings import Settings


def init_app(settings: Settings) -> pyrogram.Client:
    """Инициализация приложения"""
    logger.debug("Создаём приложение")
    app = pyrogram.Client("UserBot")

    _add_commands(app=app, settings=settings)

    return app


def _add_commands(app: pyrogram.Client, settings: Settings) -> None:
    """Добавление команд"""
    command_manager = commands.CommandManager(app=app, settings=settings)
    logger.debug("Добавляем команды")

    command_classes = _find_commands()

    for command_class in command_classes:
        command_manager.register_command(command=command_class)


def _find_commands() -> list[Type[BaseCommand]]:
    """Поиск команд в папке app.commands"""
    command_modules = _find_command_modules()
    logger.debug(f"Найдены модули в пакете с командами: {command_modules}")
    found_commands = _import_commands_from_modules(command_modules)

    return found_commands


def _find_command_modules() -> list[str]:
    """Поиск модулей в пакете app.commands"""
    logger.debug(f"Ищем команды в папке {commands.__path__}")
    modules_info = [modules_info for modules_info in pkgutil.walk_packages(commands.__path__, commands.__name__ + ".")]

    return [modules_info.name for modules_info in modules_info if not modules_info.ispkg]


def _import_commands_from_modules(modules: list[str]) -> list[Type[BaseCommand]]:
    """Импортирование команд из модулей"""
    found_commands = []
    for command_module in modules:
        for module_object_name, module_object in inspect.getmembers(importlib.import_module(command_module)):
            if _is_object_a_command_class(module_object):
                found_commands.append(module_object)
                logger.debug(f"Найдена команда: {module_object.__name__}")

    return found_commands


def _is_object_a_command_class(object_: type) -> bool:
    """Является ли объект классом команды"""
    if inspect.isclass(object_) and issubclass(object_, BaseCommand) and not inspect.isabstract(object_):
        return True

    return False
