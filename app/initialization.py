import pyrogram
from loguru import logger

from app import commands
from app.settings import Settings


def init_app(settings: Settings) -> pyrogram.Client:
    """Инициализация приложения"""
    logger.debug("Создаём приложение")
    app = pyrogram.Client("UserBot")

    _add_commands(app=app, settings=settings)

    return app


# TODO подумать, нужно ли сделать добавление команд по другому
def _add_commands(app: pyrogram.Client, settings: Settings) -> None:
    """Добавление команд"""
    command_manager = commands.CommandManager(app=app, settings=settings)
    logger.debug("Добавляем команды")

    command_manager.register_command(command=commands.TypingCommand)
    command_manager.register_command(command=commands.HackCommand)
    command_manager.register_command(command=commands.HeartCommand)
