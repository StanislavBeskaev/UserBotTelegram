import time

import pyrogram
from pyrogram.errors import FloodWait

from app.commands.base_command import BaseDotCommand


class TypingCommand(BaseDotCommand):
    """Команда для медленного набора текста"""

    @property
    def text(self) -> str:
        return "type"

    def execute(self, client: pyrogram.client.Client, message: pyrogram.types.Message) -> None:
        original_text = self._calculate_original_text(message_text=message.text)
        remaining_text = original_text
        typed_text = ""
        typing_symbol = self._settings.TYPING_SYMBOL

        while typed_text != original_text:
            try:
                message.edit(typed_text + typing_symbol)
                time.sleep(self._settings.TYPING_SYMBOL_INTERVAL)

                typed_text = typed_text + remaining_text[0]
                remaining_text = remaining_text[1:]
                self.log(f"{typed_text=}")
                self.log(f"{remaining_text=}")

                message.edit(typed_text)
                time.sleep(self._settings.TYPING_PAUSE_INTERVAL)

            except FloodWait:
                time.sleep(self._settings.FLOOD_WAIT_INTERVAL)

    def _calculate_original_text(self, message_text: str) -> str:
        original_text = message_text.split(f"{self.prefix}{self.text} ", maxsplit=1)[1]

        return original_text
