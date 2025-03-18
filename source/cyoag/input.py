import logging
from typing import Dict, List

import click
from data_models import Room


def get_valid_input(manager) -> None:
    while True:
        logging.info(f"Current room: {manager.location.name}")
        user_input: str = click.prompt(
            click.style("What do you want to do?\n", fg="green")
        )
        inputs: List[str] = user_input.split(" ")

        if inputs[0] not in ("take", "inspect", "go", "drop", "inventory"):
            logging.warning(f"Invalid command: {inputs[0]}")
            print(
                "Invalid command. Please use 'take', 'inspect', 'go', 'drop', or 'inventory'."
            )
            continue

        if len(inputs) < 2:
            command, argument = inputs[0], None
        else:
            command, argument = inputs[0], inputs[1]

        logging.debug(
            f"Player command: {command} {argument if len(inputs) > 1 else ''}"
        )

        if manager.handle_command(command, argument):
            break


def get_valid_choice(manager, choice: str) -> None:
    while True:
        event = manager.location.choices[choice]
        # TODO: Feed in choice dynamically, reformat into Events
        click.secho(event.description[0], fg="bright_white", italic=True)

        user_input: str = click.prompt(click.style("choice?", fg="green"))

        if user_input not in event.outcomes:
            print("invalid choice!")
        else:
            print("valid choice!")
            outcome = event.outcomes[user_input]
            print(outcome.description[0])
            command, argument = outcome.command, outcome.argument
            manager.handle_command(command, argument)

            break
