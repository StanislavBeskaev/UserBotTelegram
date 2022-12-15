import random
import time

import pyrogram
from pyrogram.errors import FloodWait

from app.commands.base_command import BaseDotCommand


class HackCommand(BaseDotCommand):
    """Команда для взлома пентагона(понарошку)"""

    @property
    def text(self) -> str:
        return "hack"

    @property
    def description(self) -> str:
        return "Команда для взлома пентагона (понарошку)"

    def execute(self, client: pyrogram.client.Client, message: pyrogram.types.Message) -> None:
        perc = 0

        while perc < 100:
            try:
                text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
                message.edit(text)

                perc += random.randint(1, 3)
                time.sleep(0.1)

            except FloodWait:
                time.sleep(self._settings.FLOOD_WAIT_INTERVAL)

        message.edit("🟢 Пентагон успешно взломан!")
        time.sleep(3)

        message.edit("👽 Поиск секретных данных об НЛО ...")
        perc = 0

        while perc < 100:
            try:
                text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
                message.edit(text)

                perc += random.randint(1, 5)
                time.sleep(0.15)

            except FloodWait:
                time.sleep(self._settings.FLOOD_WAIT_INTERVAL)

        message.edit("🦖 Найдены данные о существовании динозавров на земле!")
