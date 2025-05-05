# pyright: standard
import logging
import time
from typing import Dict, Optional

from readchar import readkey
from rich.console import Console

from cyoag.data_loader import DataLoader
from cyoag.data_types import Event, Room, Skin
from cyoag.input import Command, get_valid_choice, get_valid_input
from cyoag.narrator import Narrator
from cyoag.player import Player
from cyoag.command_processor import CommandProcessor

logger = logging.getLogger(__name__)
rich = Console()


class Manager:
    def __init__(self, player: Player, data_loader: DataLoader) -> None:
        self.data_loader: DataLoader = data_loader
        self.location: Optional[Room] = None
        self.player: Player = player
        self.cmd_proc = CommandProcessor(self)
        self.next_event: Optional[Event] = None
        self.narrator: Optional[Narrator] = None
        self.rooms_dict: Dict[str, Room] = {}
        self.running: bool = True
        self.status: Optional[str] = ""
        self.skins_dict: Dict[str, Skin] = {}
        self.skin: Optional[Skin] = None

    def _load_data(self) -> None:
        game_data = self.data_loader.load_data()
        self.rooms_dict = game_data["rooms"]
        self.location = self.rooms_dict[
            "start"
        ]  # TODO: get rid of magic strings
        self.next_event = self.location.events.get("event1")
        self.skins_dict = game_data["skins"]
        self.skin = self.skins_dict["default"]  # TODO: customisable
        self.narrator = Narrator(self.skin)

    def start(self) -> None:
        self._load_data()
        self.handle_narration(
            "\nCYOAG: Choose Your Own Adventure Game\n", "title"
        )

        while self.running:
            if self.location is None:
                raise RuntimeError("self.location must not be None.")
            if self.location.name == "shrine":
                self.running = False
            else:
                self.play_scene()

        self.handle_narration("\nGAME OVER!\n", "title")
        logger.info("Game closed")

    def play_scene(self) -> None:

        logger.info("Check if play next_event if exists:")

        if (
            self.next_event
            and self.next_event.trigger  # use event triggers
            and not self.next_event.played
        ):
            self.play_event()

        logger.info("Attempting to play description if required")
        self.handle_narration(self.location, "narration")
        print(*self.require_data(self.location).exits, sep=", ")

        while True:
            cmd, arg = get_valid_input()

            if cmd == "invalid":
                self.handle_narration(f"Invalid {arg}", "action")
                continue
            if self.cmd_proc.handle(cmd, arg):
                break

    def play_event(self) -> None:
        if self.next_event is None:
            raise RuntimeError(
                "next_event must be set before calling play_event()"
            )

        current_event = self.require_data(self.next_event)
        current_location = self.require_data(self.location)
        logger.info(f"Playing event: {current_event.name}")
        self.handle_narration(current_event, "narration")

        while True:
            cmd, arg, outcome = get_valid_choice(current_event)

            if cmd == "invalid":
                print(f"Invalid {arg}")
                continue
            break

        self.handle_narration(outcome, "narration")

        # todo: check logic, move to EventsManager? set from current_location.next_event?
        if not current_event.repeatable:
            current_event.played = True
            self.next_event = None
        elif current_event.next_event:
            logger.info("Setting new next_event...")
            self.next_event = current_location.events.get(
                current_event.next_event
            )
        else:
            self.next_event = None

        # wait for input and print newline
        readkey()
        rich.print()

    def handle_narration(self, entity, style: str):
        if isinstance(entity, str):
            self.narrator.say(entity, style)
            time.sleep(0.1)
        else:
            for line in entity.description:
                self.narrator.say(line, style)
                time.sleep(0.1)

    def require_data(self, value):
        if value is None:
            raise RuntimeError(f"{value} cannot be None")
        return value

    def update_items(self, item: str, action: str) -> None:
        current_location = self.require_data(self.location)

        if action == "take":
            self.player.add_item(current_location, item)
            current_location.items.pop(item)

        elif action == "drop":
            current_location.items[item] = self.player.drop_item(item)

    def handle_go(self, exit: str) -> bool:
        current_location = self.require_data(self.location)

        if exit not in current_location.exits:
            self.handle_narration(f"Cannot find {exit}!", "action")
            logger.info(f"Player tried to go to an invalid exit: {exit}")
            return False

        logger.info(f"(manager.py) Updating manager.location to: {exit}")
        self.location = self.rooms_dict[exit]
        self.status = "entered"
        logger.info(
            f"(manager.py) manager.location successfully updated to: {exit}"
        )
        return True

    def handle_take(self, item: str) -> bool:
        current_location = self.require_data(self.location)

        if item not in current_location.items:
            self.narrator.say(f"You cannot find the {item}!", "action")
            logger.info(f"Player tried to take an invalid item: {item}")
            return False

        logger.info(f"Player found item: {item}")
        self.update_items(item, "take")
        self.handle_narration(f"You take the {item}!", "action")

        inventory_items = ", ".join(self.player.items.keys())
        logger.info(f"Player's inventory after taking item: {inventory_items}")
        return False

    def handle_drop(self, item: str) -> bool:
        if item not in self.player.items:
            self.handle_narration(f"{item} not in your inventory", "action")
            logger.info(
                f"Player tried to drop an item not in inventory: {item}"
            )
            return False

        self.handle_narration(f"You drop the {item}!", "action")
        logger.info(f"Player dropped item: {item}")
        self.update_items(item, "drop")
        return False

    def handle_examine(self, item: Optional[str]) -> bool:
        current_location = self.require_data(self.location)
        logger.info(f"Handle command item: {item}")

        if not item:
            logger.info("Player examined room")
            self.handle_narration(current_location, "narration")
        elif (
            item not in current_location.items
            and item not in self.player.items
        ):
            logger.debug(f"Player tried to examine an invalid item: {item}")
            self.handle_narration(f"You can't find the {item} here.", "action")
        elif item in self.player.items:
            logger.info(f"Player examined item in inventory: {item}")
            self.handle_narration(self.player.items[item], "narration")
        elif item in current_location.items:
            logger.info(f"Player examined item in room: {item}")
            self.handle_narration(current_location.items[item], "narration")
        return False

    def handle_inventory(self, argument: Optional[str]) -> bool:
        if not self.player.items:
            logger.info("Player checked inventory: empty")
            self.handle_narration("Your inventory is empty!", "action")
            return False

        logger.info("Player checked inventory")
        inventory_text = "\n".join(f"- {item}" for item in self.player.items)
        self.handle_narration(inventory_text, "action")
        return False

    def handle_help(self, argument: Optional[str]) -> bool:
        self.handle_narration(
            ", ".join([cmd.value for cmd in Command]), "action"
        )
        return False


# required rebuild as event uses forward reference to manager in the trigger func lambda
Event.model_rebuild()
