import logging

from rich.console import Console
from rich.theme import Theme

from cyoag.data_types import Skin

logger = logging.getLogger(__name__)


class Narrator:
    def __init__(self, skin: Skin) -> None:
        logger.debug(type(skin))
        self.skin: Theme = Theme(skin.__dict__)
        self.console: Console = Console(theme=self.skin)

    def say(self, txt: str, style: str):
        self.console.print(txt, style=style, markup=False, highlight=False)
