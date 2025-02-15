from player import Player
from rooms import Room
# from manager import MANAGER, Manager
import click


def get_valid_input(PLAYER: Player, current_room: Room, MANAGER) -> None:
    while True:
        user_input: str = click.prompt(click.style("What do you want to do?\n", fg='green'))
        inputs: list[str] = user_input.split(" ")

        if inputs[0] not in ("take", "inspect", "go"):
            print("Invalid command. Please use 'take', 'inspect' or 'go'.\nTake and inspect not fully implemented.")
            continue

        if len(inputs) < 2:
            print(f"Missing argument. The {inputs[0]} command requires an argument.")
            continue

        command, argument = inputs[0], inputs[1]

        if command == "take":
            if argument not in current_room.items:
                click.secho(f"(input.py) {argument} is not a valid item...", fg='red')
                continue
            else:
                click.secho(f"(input.py) {argument} is a valid item...", fg='red')
                click.secho(f"You take the {argument}!", fg='green')
                MANAGER.update_items(argument, PLAYER)
                continue

        elif command == "inspect":
            click.secho(f"(input.py) Checking if {argument} is a valid item...", fg='red')
            # PLAYER.inspect(argument)
            continue

        elif command == "go":
            if argument not in current_room.exits:
                click.secho(f"(input.py) {argument} is not a valid exit!", fg='red')
                continue
            else:
                click.secho(f"(input.py) {argument} is a valid exit.", fg='red')
                MANAGER.update_location(argument)
                break


def get_valid_choice(PLAYER: Player, current_room: Room) -> None:
    while True:
        user_input: str = click.prompt(click.style("choice?", fg='green'))
        if user_input not in current_room.choice:
            print("Invalid choice. Try again..")
            continue
        else:
            print(f"You've got the {user_input}")
            break