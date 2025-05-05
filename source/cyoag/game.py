# pyright: standard
import logging

import click

from cyoag.data_loader import DataLoader
from cyoag.manager import Manager

# from cyoag.narrator import Narrator
from cyoag.player import Player


@click.command()
@click.option("--log-level", default="info")
def play_game(log_level: str) -> None:

    log_level = getattr(logging, log_level.upper())
    logging.basicConfig(
        level=log_level, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    player: Player = Player()
    data_loader: DataLoader = DataLoader()
    manager: Manager = Manager(player, data_loader)
    manager.start()


if __name__ == "__main__":
    play_game()
