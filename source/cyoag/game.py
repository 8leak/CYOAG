import logging
import sys

import click
from input import get_valid_choice, get_valid_input
from manager import Manager
from player import Player

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


@click.command()
def initiate() -> None:
    # logging.info("Game initiated")
    # click.secho("Welcome to the game!\n", fg="bright_white", bold=True)

    # choice: str = click.prompt(
    #     click.style("Would you like to play, yes or no?\n", fg="green", bold=True)
    # )
    # if choice == "no":
    #     input("Press any key to quit.")
    #     sys.exit()
    # else:
        play_game()



@click.command()
def play_game() -> None:
    game_running: bool = True
    player: Player = Player()
    manager: Manager = Manager(player)
    manager._load_data()

    # click.secho("Commands: go, take, inspect", fg="cyan")

    while game_running:
        current_room = manager.location

        # print(current_room.choices["choice1"].outcomes)
        
        if current_room.name == "shrine":
            game_running = False
        else:
            manager.play_scene(player, current_room, manager)

    click.secho("\nGAME OVER!\n", fg="bright_white", bold=True, underline=True)
    logging.info("Game closed")


initiate()

# TODO: Random element, enemy, item, stage?
# TODO: Loop? Locked in room until find key
