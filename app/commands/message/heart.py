import pyrogram
from loguru import logger

from app.commands.base_command import BaseDotCommand


class HeartCommand(BaseDotCommand):
    """Команда для рисования сердечка"""

    @property
    def text(self) -> str:
        return "heart"

    @property
    def default_symbol(self) -> str:
        return "*"

    @property
    def description(self) -> str:
        return f"Команда для рисования сердечка с указанным символом (по умолчанию {self.default_symbol})"

    @property
    def filters(self) -> pyrogram.filters.Filter:
        return pyrogram.filters.command(self.text, prefixes=self.prefix) & pyrogram.filters.me

    def execute(self, client: pyrogram.client.Client, message: pyrogram.types.Message) -> None:
        symbol = (
            message.text[len(f"{self.full_text} ")]
            if len(message.text) >= len(self.full_text) + 1
            else self.default_symbol
        )
        self.log(f"{symbol=}")
        # TODO придумать общий алгоритм для рисования сердец побольше
        heart_inner_content = '\n'.join(
            ' '.join(*zip(*row))
            for row in (
                [
                    [
                        symbol
                        if row == 0 and col % 3 != 0 or row == 1 and col % 3 == 0 or row - col == 2 or row + col == 8
                        else " "
                        for col in range(7)
                    ]
                    for row in range(6)
                ]
            )
        )
        heart_str = f"`{heart_inner_content}`"
        message.edit(heart_str)
