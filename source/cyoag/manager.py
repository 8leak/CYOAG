import logging
from typing import List
import json
import click
import input
import pathlib
import os
from typing import Dict, List
from pydantic import BaseModel, ConfigDict

from player import Player
# from rooms import Room, rooms
from data_models import Choice, Item, Room


class Manager:
    def __init__(self, player: Player) -> None:
        self.rooms: Dict[str, Room]
        self.location: Room
        # self.items: List[str] = self.location.items
        self.items: List[str]
        self.player: Player = player
    
    def _load_data(self) -> None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "data")

        with open(json_path, "r") as file:
            choices_data: List[Choice] = [Choice(**choices) for choices in json.load(file)]
        self.choices: Dict[str, Choice] = {choices.name: choices for choices in choices_data}

        with open(json_path, "r") as file:
            items_data: List[Item] = [Item(**items) for items in json.load(file)]
        self.items: Dict[str, Item] = {items.name: items for items in items_data}

        with open(json_path, "r") as file:
            rooms_data: List[Room] = [Room(**room) for room in json.load(file)]

        self.rooms: Dict[str, Room] = {room.name: room for room in rooms_data}
        for room in self.rooms.values():
            room.items = {item: self.items[item] for item in room.item_list}
            room.choices = {choice: self.choices[choice] for choice in room.choice_list}
        self.location: Room = self.rooms["start"]


    def start():
        pass

    def play_description(self, player: Player, current_room: Room) -> None:
        for description in current_room.description:
            click.secho(description, fg="bright_white", italic=True)
        print(*current_room.exits, sep="\n")

    def play_choice(self, player: Player, current_room: Room, manager) -> None:
        logging.info("Attempting to play choice.")
        # todo: handle multiple choice events
        if len(current_room.choice_list) == 1:
            input.get_valid_choice(player, current_room, manager)

    def play_scene(self, player: Player, current_room: Room, manager) -> None:
        self.play_description(player, current_room)
        self.play_choice(player, current_room, manager)
        input.get_valid_input(player, current_room, manager)

    def update_location(self, exit: str) -> None:
        logging.info(f"(manager.py) Updating manager.location to: {exit}")
        self.location = rooms[exit]
        self.items = self.location.items
        logging.info(f"(manager.py) manager.location successfully updated to: {exit}")

    def update_items(self, current_room: Room, item: str, player, action: str) -> None:
        if action == "take":
            player.add_item(current_room, item)
            self.items.pop(item)

        elif action == "drop":
            self.items[item] = player.drop_item(current_room, item)
