import json
import logging
import time
from pathlib import Path
from typing import Dict, List

from rich.console import Console

from cyoag.data_models import Event, Item, Room
from cyoag.input import Command, get_valid_choice, get_valid_input
from cyoag.player import Player
from cyoag.theme import Narrator, theme_1

rich = Console(theme=theme_1)


class Manager:
    def __init__(self, player: Player, narrator: Narrator) -> None:
        self.location: Room = None
        self.items: List[str] = []
        self.player: Player = player
        self.next_event: Event = None
        self.narrator: Narrator = narrator
        self.rooms: Dict[str, Room] = {}
        self.running: bool = True

    def _load_data(self) -> None:
        current_dir = Path(__file__).resolve().parent
        json_path = current_dir / "data"

        with open(json_path / "events.json", "r") as file:
            events_data: List[Event] = [
                Event(**events) for events in json.load(file)
            ]

        events_dict: Dict[str, Event] = {
            events.name: events for events in events_data
        }

        with open(json_path / "items.json", "r") as file:
            items_data: List[Item] = [
                Item(**items) for items in json.load(file)
            ]
        items_dict: Dict[str, Item] = {
            items.name: items for items in items_data
        }

        with open(json_path / "rooms.json", "r") as file:
            rooms_data: List[Room] = [Room(**room) for room in json.load(file)]

        self.rooms: Dict[str, Room] = {room.name: room for room in rooms_data}

        for room in self.rooms.values():
            room.items = {item: items_dict[item] for item in room.item_list}
            room.events = {
                event: events_dict[event] for event in room.event_list
            }

        self.location: Room = self.rooms["start"]
            
    # def trigger_func_constructor(self, trigger_data):
        



    def handle_narration(self, entity, style: str):
        if isinstance(entity, str):
            self.narrator.say(entity, style)
            time.sleep(0.1)
        else:
            for line in entity.description:
                self.narrator.say(line, style)
                time.sleep(0.1)

    def start(self) -> None:
        self.handle_narration(
            "\nCYOAG: Choose Your Own Adventure Game\n", "title"
        )
        while self.running:
            if self.location.name == "shrine":
                self.running = False
            else:
                self.play_scene()

        self.handle_narration("\nGAME OVER!\n", "title")
        logging.info("Game closed")

    def play_description(self) -> None:
        self.handle_narration(self.location, "narration")
        print(*self.location.exits, sep=", ")

    def play_event(self) -> None:
        logging.info("Attempting to play event.")

        if len(self.location.event_list) == 1:
            event = self.location.event_list[0]
            event = self.location.events[event]

            rich.print()
            self.handle_narration(event, "narration")

            outcome = get_valid_choice(self, event)
            self.handle_narration(outcome, "narration")

    def play_scene(self) -> None:
        # get_valid_choice(self)
        self.play_description()
        get_valid_input(self)

    def handle_command(self, command, argument):
        if command == Command.TAKE:
            self.handle_take(argument)
        elif command == Command.EXAMINE:
            self.handle_examine(argument)
        elif command == Command.GO:
            if self.handle_go(argument):
                return True
        elif command == Command.DROP:
            self.handle_drop(argument)
        elif command == Command.INVENTORY:
            self.handle_inventory()
        elif command == Command.HELP:
            self.handle_help()

    def update_items(self, item: str, action: str) -> None:
        if action == "take":
            self.player.add_item(self.location, item)
            self.location.items.pop(item)

        elif action == "drop":
            self.location.items[item] = self.player.drop_item(item)

    def handle_go(self, exit: str) -> bool:
        if exit not in self.location.exits:
            self.handle_narration(f"Cannot find {exit}!", "action")
            logging.info(f"Player tried to go to an invalid exit: {exit}")
            return False
        else:
            logging.info(f"Player found exit: {exit}")
            logging.info(f"(manager.py) Updating manager.location to: {exit}")
            self.location = self.rooms[exit]
            logging.info(
                f"(manager.py) manager.location successfully updated to: {exit}"
            )

            return True

    def handle_take(self, item: str) -> None:
        if item not in self.location.items:
            self.narrator.say(f"You cannot find the {item}!", "action")
            logging.info(f"Player tried to take an invalid item: {item}")
        else:
            logging.info(f"Player found item: {item}")
            self.update_items(item, "take")
            self.handle_narration(f"You take the {item}!", "action")

            inventory_items = ", ".join(self.player.items.keys())
            logging.info(
                f"Player's inventory after taking item: {inventory_items}"
            )

    def handle_drop(self, item: str) -> None:
        if item not in self.player.items:
            self.handle_narration(f"{item} not in your inventory", "action")
            logging.info(
                f"Player tried to drop an item not in inventory: {item}"
            )
        else:
            self.handle_narration(f"You drop the {item}!", "action")
            logging.info(f"Player dropped item: {item}")
            self.update_items(item, "drop")

    def handle_examine(self, item: str) -> None:
        if item not in self.location.items and item not in self.player.items:
            logging.debug(f"Player tried to examine an invalid item: {item}")
            self.handle_narration(f"You can't find the {item} here.", "action")
        elif item in self.player.items:
            logging.info(f"Player examined item in inventory: {item}")
            self.handle_narration(self.player.items[item], "narration")
        elif item in self.location.items:
            logging.info(f"Player examined item in room: {item}")
            self.handle_narration(self.location.items[item], "narration")

    def handle_inventory(self) -> List[str]:
        if len(self.player.items) >= 1:
            logging.info("Player checked inventory")
            for item in self.player.items:
                self.handle_narration(f"- {item}", "action")
        else:
            logging.info("Player checked inventory:  empty")
            self.handle_narration("Your inventory is empty!", "action")

    def handle_help(self) -> None:
        self.handle_narration(
            ", ".join([cmd.value for cmd in Command]), "action"
        )
