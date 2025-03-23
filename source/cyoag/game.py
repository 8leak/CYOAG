import logging

import click
from manager import Manager
from player import Player

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


@click.command()
def play_game() -> None:
    player: Player = Player()
    manager: Manager = Manager(player)
    manager._load_data()
    manager.start()


play_game()

# TODO: Random element, enemy, item, stage?
# TODO: Loop? Locked in room until find key