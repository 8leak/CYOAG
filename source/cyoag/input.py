import logging
from enum import Enum
from typing import List

import click
from cyoag.theme import theme_1

from rich.console import Console
rich = Console(theme=theme_1)


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

        user_input: str = rich.input("[info]\nWhat do you want to do?\n[/]")

        inputs: List[str] = user_input.lower().split()

        command = INPUTS.get(inputs[0])

        if command is None:
            rich.print(f"Invalid command: {inputs[0]}")
            continue

        argument = inputs[1] if len(inputs) > 1 else None

        if manager.handle_command(command, argument):
            break


def get_valid_choice(manager, choice: str) -> None:
    while True:
        event = manager.location.choices[choice]
        # TODO: Feed in choice dynamically, reformat into Events
        rich.print(f"[i bright_white]{event.description[0]}[/]")

        user_input: str = rich.input("[info]Make your choice...\n[/]")

        if user_input not in event.outcomes:
            rich.print("invalid choice!")
        else:
            logging.info("valid choice![/]")
            outcome = event.outcomes[user_input]
            command, argument = INPUTS.get(outcome.command), outcome.argument
            manager.handle_command(command, argument)
            rich.print(outcome.description[0], style="narration")

            break
