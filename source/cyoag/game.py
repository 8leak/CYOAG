# pyright: standard

import logging

import click

from cyoag.manager import Manager
from cyoag.player import Player
from cyoag.theme import Narrator, theme_1
from cyoag.data_loader import DataLoader


@click.command()
@click.option("--log-level", default="info")
def play_game(log_level: str) -> None:

    log_level = getattr(logging, log_level.upper())
    logging.basicConfig(
        level=log_level, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    player: Player = Player()
    narrator: Narrator = Narrator(theme_1)
    data_loader: DataLoader = DataLoader()
    manager: Manager = Manager(player, narrator, data_loader)
    manager.start()


if __name__ == "__main__":
    play_game()
