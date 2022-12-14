from loguru import logger

from app.initialization import init_app
from app.settings import get_settings


# TODO написать readme, указать переменные окружения
# TODO рефакторинг, разделение по частям
# TODO docker
def main():
    logger.debug("Старт")

    settings = get_settings()
    _write_pyrogram_config(api_id=settings.TG_API_ID, api_hash=settings.TG_API_HASH)

    app = init_app(settings=settings)
    logger.info("Запускаем UserBot")
    app.run()


def _write_pyrogram_config(api_id: str, api_hash: str):
    logger.debug("Записываем pyrogram config")

    with open('config.ini', mode='w', encoding='UTF-8') as config:
        config_content = f"""[pyrogram]\napi_id = {api_id}\napi_hash = {api_hash}"""
        config.write(config_content)

    logger.debug("pyrogram config записан")


if __name__ == "__main__":
    main()
