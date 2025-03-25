import logging

import click

from cyoag.manager import Manager
from cyoag.player import Player


@click.command()
@click.option("--log-level", default="warning")
def play_game(log_level) -> None:

    log_level = getattr(logging, log_level.upper())
    logging.basicConfig(
        level=log_level, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    player: Player = Player()
    manager: Manager = Manager(player)
    manager._load_data()
    manager.start()


if __name__ == "__main__":
    play_game()
