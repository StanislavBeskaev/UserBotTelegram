import time

import pyrogram
import requests
from loguru import logger

from app.commands.base_command import BaseExclamationMarkCommand


# TODO подумать об декораторе для регистрации команды
class CatCommand(BaseExclamationMarkCommand):
    """Команда для отправки котика"""

    CUTE_CAT_URL = "https://cataas.com/cat/cute"
    TEMP_CAT_FILE = "tmp_cat.jpeg"

    @property
    def text(self) -> str:
        return "cat"

    @property
    def description(self) -> str:
        return self.__doc__

    def execute(self, client: pyrogram.client.Client, message: pyrogram.types.Message) -> None:
        message.edit("Выбираю котика, ждите...")
        try:
            self._download_cat()
            time.sleep(0.5)
            message.reply_photo(photo=self.TEMP_CAT_FILE)  # TODO посмотреть как можно посылать без сохранения на диск
            message.delete()
        except Exception as e:
            logger.error(f"Не удалось скачать котика: {e}")
            message.edit("Котика нет(")

    def _download_cat(self) -> None:
        response = requests.get(self.CUTE_CAT_URL)
        response.raise_for_status()
        with open(self.TEMP_CAT_FILE, mode="wb") as file:
            file.write(response.content)
