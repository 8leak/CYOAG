import logging
from enum import Enum
from typing import List

import click


class Command(Enum):
    GO = "go"
    TAKE = "take"
    EXAMINE = "examine"
    DROP = "drop"
    INVENTORY = "inventory"
    HELP = "help"


INPUTS = {
    "go": Command.GO,
    "take": Command.TAKE,
    "examine": Command.EXAMINE,
    "look": Command.EXAMINE,
    "drop": Command.DROP,
    "inventory": Command.INVENTORY,
    "i": Command.INVENTORY,
    "help": Command.HELP,
    "commands": Command.HELP,
}


def get_valid_input(manager) -> None:
    while True:
        logging.info(f"Current room: {manager.location.name}")

        user_input: str = click.prompt(
            click.style("What do you want to do?\n", fg="green")
        )

        inputs: List[str] = user_input.lower().split()

        command = INPUTS.get(inputs[0])

        if command is None:
            print(f"Invalid command: {inputs[0]}")
            continue

        argument = inputs[1] if len(inputs) > 1 else None

        if manager.handle_command(command, argument):
            break


def get_valid_choice(manager, choice: str) -> None:
    while True:
        event = manager.location.choices[choice]
        # TODO: Feed in choice dynamically, reformat into Events
        click.secho(event.description[0], fg="bright_white", italic=True)

        user_input: str = click.prompt(click.style("Make your choice:", fg="green"))

        if user_input not in event.outcomes:
            print("invalid choice!")
        else:
            print("valid choice!")
            outcome = event.outcomes[user_input]
            print(outcome.description[0])
            command, argument = outcome.command, outcome.argument
            manager.handle_command(command, argument)

            break
