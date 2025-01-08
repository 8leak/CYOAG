from player import Player
from rooms import Room
from manager import MANAGER, Manager
import click


def get_valid_input(PLAYER: Player, current_room: Room) -> None:
    while True:
        user_input: str = input("")
        inputs: list[str] = user_input.split(" ")

        if inputs[0] not in ("take", "inspect", "go"):
            print(
                "Invalid command. Please use 'take', 'inspect' or 'go'.\nTake and inspect not implemented."
            )
            continue

        if len(inputs) < 2:
            print(f"Missing argument. The {inputs[0]} command requires an argument.")
            continue

        command, argument = inputs[0], inputs[1]

        if command == "take":
            print("takin some shit")
            # PLAYER.take(argument)
            break

        elif command == "inspect":
            print("inspectin some shit")
            # PLAYER.inspect(argument)
            break

        elif command == "go":
            click.secho(f"(input.py) Checking if {argument} is a valid exit...", fg='red')
            if argument not in current_room.exits:
                click.secho(f"(input.py) {argument} is not a valid exit!", fg='red')
                continue
            else:
                click.secho(f"(input.py) {argument} is a valid exit.", fg='red')
                MANAGER.update_location(argument)
                break