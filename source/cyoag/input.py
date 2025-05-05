# pyright: strict
import logging
from typing import TYPE_CHECKING, Any, List

from rich.console import Console

from cyoag.data_types import Command, Event

if TYPE_CHECKING:
    pass


rich = Console()

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


def get_valid_input() -> Any:
    user_input: str = rich.input("\n>")
    if not user_input:
        return "invalid", "input"

    inputs: List[str] = user_input.lower().split()
    command = INPUTS.get(inputs[0])

    if command is None:
        return "invalid", "command"

    argument = inputs[1] if len(inputs) > 1 else None
    return command, argument


def get_valid_choice(event: Event) -> Any:
    user_input: str = rich.input("\n>")

    outcome = event.outcomes.get(user_input)
    if outcome is None:
        return "invalid", "choice", "none"

    logging.info("Valid choice!")
    command, argument = (
        INPUTS.get(outcome.command),
        outcome.argument,
    )

    if command is None:
        raise ValueError(f"Invalid command in outcome: {outcome.command}")

    return command, argument, outcome
