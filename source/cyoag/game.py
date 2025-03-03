from player import PLAYER
from rooms import ROOMS
from manager import MANAGER, Manager
from input import get_valid_input, get_valid_choice
import click

@click.command()
def initiate() -> None:
    choice: str = click.prompt(click.style("Would you like to play, yes or no?\n", fg='green'))
    if choice == "no":
        input("Press any button to quit.")
        exit()
    else:
        play_game()


@click.command()
def play_game() -> None:
    game_running: bool = True
    
    click.secho("Commands: go, take, inspect", fg='cyan')

    while game_running:
        current_room = MANAGER.location
        click.secho(f"(game.py) Set current location to: {current_room.name}\n", fg='red')
        
        if current_room.name == "shrine":
            game_running = False
            click.secho("(game.py) current location is shrine, I should be quitting!", fg='red')
        else:
            MANAGER.play_scene(PLAYER, current_room)

    click.secho("\nGAME OVER!\n", fg='bright_white', bold=True, underline=True)

# hello()
initiate()

# TODO: Random element, enemy, item, stage?
# TODO: Loop? Locked in room until find key