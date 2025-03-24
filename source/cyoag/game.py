import logging

import click

from cyoag.manager import Manager
from cyoag.player import Player

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


@click.command()
def play_game() -> None:
    player: Player = Player()
    manager: Manager = Manager(player)
    manager._load_data()
    manager.start()


if __name__ == "__main__":
    play_game()
