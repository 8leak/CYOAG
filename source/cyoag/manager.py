import json
import logging
from pathlib import Path
from typing import Dict, List

from cyoag.theme import theme_1
from cyoag.data_models import Choice, Item, Room
from cyoag.input import Command, get_valid_choice, get_valid_input
from cyoag.player import Player

import click
from rich.console import Console
rich = Console(theme=theme_1)

class Manager:
    def __init__(self, player: Player) -> None:
        self.location: Room = None
        self.items: List[str] = []
        self.player: Player = player
        self.rooms: Dict[str, Room] = {}
        self.running: bool = True

    def _load_data(self) -> None:
        current_dir = Path(__file__).resolve().parent
        json_path = current_dir / "data"

        with open(json_path / "choices.json", "r") as file:
            choices_data: List[Choice] = [
                Choice(**choices) for choices in json.load(file)
            ]
        choices_dict: Dict[str, Choice] = {
            choices.name: choices for choices in choices_data
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
            room.choices = {
                choice: choices_dict[choice] for choice in room.choice_list
            }

        self.location: Room = self.rooms["start"]

    def start(self) -> None:
        while self.running:
            if self.location.name == "shrine":
                self.running = False
            else:
                self.play_scene()

        click.secho(
            "\nGAME OVER!\n", fg="bright_white", bold=True, underline=True
        )
        logging.info("Game closed")

    def play_description(self) -> None:
        for description in self.location.description:
            rich.print(description, style="narration")
        print(*self.location.exits, sep=", ")

    def play_choice(self) -> None:
        logging.info("Attempting to play choice.")
        # todo: handle multiple choice events
        if len(self.location.choice_list) == 1:
            choice = self.location.choice_list[0]
            get_valid_choice(self, choice)

    def play_scene(self) -> None:
        self.play_description()
        self.play_choice()
        get_valid_input(self)

    def update_items(self, item: str, action: str) -> None:
        if action == "take":
            self.player.add_item(self.location, item)
            self.location.items.pop(item)

        elif action == "drop":
            self.location.items[item] = self.player.drop_item(item)

    def handle_go(self, exit: str) -> bool:
        if exit not in self.location.exits:
            click.secho(f"Cannot find {exit}!", fg="green")
            logging.warning(f"Player tried to go to an invalid exit: {exit}")
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
            click.secho(f"You cannot find the {item}!", fg="green")
            logging.warning(f"Player tried to take an invalid item: {item}")
        else:
            logging.info(f"Player found item: {item}")
            self.update_items(item, "take")
            rich.print(f"You take the {item}!", style="action")

            inventory_items = ", ".join(self.player.items.keys())
            logging.info(
                f"Player's inventory after taking item: {inventory_items}"
            )

    def handle_drop(self, item: str) -> None:
        if item not in self.player.items:
            click.secho(f"{item} not in your inventory")
            logging.warning(
                f"Player tried to drop an item not in inventory: {item}"
            )
        else:
            click.secho(f"You drop the {item}!", fg="green")
            logging.info(f"Player dropped item: {item}")
            self.update_items(item, "drop")

    def handle_examine(self, item: str) -> None:
        if item not in self.location.items and item not in self.player.items:
            logging.debug(f"Player tried to examine an invalid item: {item}")
            click.secho(f"You can't find the {item} here.", fg="red")
        elif item in self.player.items:
            logging.info(f"Player examined item in inventory: {item}")
            click.secho(
                self.player.items[item].description[0],
                fg="bright_white",
                italic=True,
            )
        elif item in self.location.items:
            logging.info(f"Player examined item in room: {item}")
            click.secho(
                self.location.items[item].description[0],
                fg="bright_white",
                italic=True,
            )

    def handle_inventory(self) -> List[str]:
        if len(self.player.items) >= 1:
            logging.info("Player checked inventory")
            print("Inventory:")
            for item in self.player.items:
                print(f"- {item}")
        else:
            logging.info("Player checked inventory: empty")
            print("Your inventory is empty!")

    def handle_help(self) -> None:
        click.secho(
            f"Commands: {', '.join([cmd.value for cmd in Command])}",
            fg="white",
        )

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
