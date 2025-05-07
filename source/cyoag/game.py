# pyright: standard
import logging

import click

from cyoag.data_loader import DataLoader
from cyoag.game_data import GameData
from cyoag.manager import Manager
from cyoag.player import Player


@click.command()
@click.option("--log-level", default="info")
def play_game(log_level: str) -> None:

    log_level = getattr(logging, log_level.upper())
    logging.basicConfig(
        level=log_level, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    game_data = GameData(DataLoader())
    manager = Manager(Player(), game_data)
    manager.start()


if __name__ == "__main__":
    play_game()
