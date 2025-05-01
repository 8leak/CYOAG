# pyright: strict
import logging
from enum import Enum
from typing import TYPE_CHECKING, List

from rich.console import Console

from cyoag.data_models import Event, Outcome
from cyoag.narrator import theme_1

if TYPE_CHECKING:
    from cyoag.manager import Manager


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


def get_valid_input(manager: "Manager") -> None:
    while True:
        assert manager.location is not None, "manager.location cannot be None"
        logging.info(f"Current room: {manager.location.name}")

        user_input: str = rich.input("\n>")
        if not user_input:
            continue

        inputs: List[str] = user_input.lower().split()
        command = INPUTS.get(inputs[0])

        if command is None:
            rich.print(f"Invalid command: {inputs[0]}")
            continue

        argument = inputs[1] if len(inputs) > 1 else None

        if manager.handle_command(command, argument):
            break


def get_valid_choice(manager: "Manager", event: Event) -> Outcome:
    while True:
        user_input: str = rich.input("\n>")

        outcome = event.outcomes.get(user_input)
        if outcome is None:
            rich.print("Invalid choice!")
            continue
        else:
            logging.info("Valid choice!")
            command, argument = INPUTS.get(outcome.command), outcome.argument

            if command is None:
                raise ValueError(
                    f"Invalid command in outcome: {outcome.command}"
                )
            manager.handle_command(command, argument)
            return outcome
