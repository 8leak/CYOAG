import logging
from typing import List

import click
import input
from player import Player, player
from rooms import Room, rooms


class Manager:
    def __init__(self) -> None:
        self.location: Room = rooms["start"]
        self.items: List[str] = self.location.items
        self.player: Player = player

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


manager: Manager = Manager()
