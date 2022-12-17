import time

import pyrogram
from loguru import logger

from app.commands.base_command import BaseExclamationMarkCommand
from app.commands.interactive.anecdotes_handlers import get_anecdote


class JokeCommand(BaseExclamationMarkCommand):
    """Команда для отображения анекдота"""

    @property
    def text(self) -> str:
        return "joke"

    def execute(self, client: pyrogram.client.Client, message: pyrogram.types.Message) -> None:
        message.edit("Выбираю случайный анекдот")
        anecdote_result = get_anecdote()
        logger.debug(f"{anecdote_result=}")
        if anecdote_result.success:
            anecdote_text = f'{anecdote_result.text}\n\nИсточник: {anecdote_result.source}'
        else:
            anecdote_text = 'Не удалось получить анекдот'
        logger.info(anecdote_text)
        time.sleep(self._settings.JOKE_CHOICE_INTERVAL)
        message.edit(anecdote_text)
