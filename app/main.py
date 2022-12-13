import random
from time import sleep

import daemon
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from app.settings import get_settings, Settings

app = Client("my_account")


# TODO написать readme
# TODO рефакторинг, разделение по частям
# TODO type hints
# TODO docker
# TODO добавить описания
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def typing(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while tbp != orig_text:
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.02)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait:
            sleep(0.05)


# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0

    while perc < 100:
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 3)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)

    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0

    while perc < 100:
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 5)
            sleep(0.15)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")


def main():
    # TODO возможно использование punq
    settings = get_settings()
    _check_settings(settings=settings)

    _write_pyrogram_config(api_id=settings.TG_API_ID, api_hash=settings.TG_API_HASH)
    app.run()


def _check_settings(settings: Settings) -> None:

    if not settings.TG_API_ID:
        print("Укажите api_id в переменной окружения TG_API_ID")
        exit(1)
    if not settings.TG_API_HASH:
        print("Укажите api_hash в переменной окружения TG_API_HASH")
        exit(1)


def _write_pyrogram_config(api_id: str, api_hash: str):
    with open('config.ini', mode='w', encoding='UTF-8') as config:
        config_content = f"[pyrogram]\napi_id = {api_id}\napi_hash = {api_hash}"
        config.write(config_content)


if __name__ == "__main__":
    with daemon.DaemonContext():
        main()
