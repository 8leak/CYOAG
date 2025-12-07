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
    "use": Command.USE,
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

    rest = inputs[1:]

    if command is Command.USE:
        if "on" in rest:
            on_index = rest.index("on")
            item_words = rest[:on_index]
            target_words = rest[on_index + 1 :]

            item = " ".join(item_words) if item_words else None
            target = " ".join(target_words) if target_words else None

            argument = (item, target)
        else:
            item = " ".join(rest) if rest else None
            argument = (item, None)

        return command, argument

    argument = " ".join(rest) if rest else None
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
