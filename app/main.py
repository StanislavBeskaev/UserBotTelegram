import random
from time import sleep

import pyrogram
from pyrogram import filters
from pyrogram.errors import FloodWait
from loguru import logger

from app.settings import get_settings, Settings
from app.enum import CommandEnum

app = pyrogram.Client("my_account")

COMMAND_PREFIX = "."


# TODO написать readme
# TODO рефакторинг, разделение по частям
# TODO docker
@app.on_message(filters.command(CommandEnum.TYPING, prefixes=COMMAND_PREFIX) & filters.me)
def typing(client: pyrogram.client.Client, message: pyrogram.types.Message):
    """Команда для медленного набора текста"""
    logger.debug(f"typing, text={message.text} {client=} {message=}")
    orig_text = message.text.split(f"{COMMAND_PREFIX}{CommandEnum.TYPING} ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while tbp != orig_text:
        try:
            message.edit(tbp + typing_symbol)
            sleep(0.02)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            message.edit(tbp)
            sleep(0.05)

        except FloodWait:
            sleep(0.05)


@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(client: pyrogram.client.Client, message: pyrogram.types.Message):
    """Команда взлома пентагона)"""
    perc = 0

    while perc < 100:
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            message.edit(text)

            perc += random.randint(1, 3)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    message.edit("🟢 Пентагон успешно взломан!")
    sleep(3)

    message.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0

    while perc < 100:
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            message.edit(text)

            perc += random.randint(1, 5)
            sleep(0.15)

        except FloodWait as e:
            sleep(e.x)

    message.edit("🦖 Найдены данные о существовании динозавров на земле!")


def main():
    logger.debug("Старт")

    settings = get_settings()
    _check_settings(settings=settings)

    _write_pyrogram_config(api_id=settings.TG_API_ID, api_hash=settings.TG_API_HASH)

    logger.info("Запускаем UserBot")
    app.run()


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


def _write_pyrogram_config(api_id: str, api_hash: str):
    logger.debug("Записываем pyrogram config")

    with open('config.ini', mode='w', encoding='UTF-8') as config:
        config_content = f"""[pyrogram]\napi_id = {api_id}\napi_hash = {api_hash}"""
        config.write(config_content)

    logger.debug("pyrogram config записан")


if __name__ == "__main__":
    main()
