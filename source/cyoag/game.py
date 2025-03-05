from player import player
from rooms import rooms
from manager import manager, Manager
from input import get_valid_input, get_valid_choice
import click
from item import Item, items

@click.command()
def initiate() -> None:
    click.secho("Welcome to the game!\n", fg='bright_white', bold=True)
    
    print(player.items)

    choice: str = click.prompt(click.style("Would you like to play, yes or no?\n", fg='green', bold=True))
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
        current_room = manager.location
        click.secho(f"(game.py) Set current location to: {current_room.name}\n", fg='red')
        
        if current_room.name == "shrine":
            game_running = False
            click.secho("(game.py) current location is shrine, I should be quitting!", fg='red')
        else:
            manager.play_scene(player, current_room)

    click.secho("\nGAME OVER!\n", fg='bright_white', bold=True, underline=True)

# hello()
initiate()

# TODO: Random element, enemy, item, stage?
# TODO: Loop? Locked in room until find key