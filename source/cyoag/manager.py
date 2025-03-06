from player import player, Player
from rooms import rooms, Room
from typing import List
import input
import click

class Manager:
    def __init__(self) -> None:
        self.location: Room = rooms["start"]
        self.items: List[str] = self.location.items
        self.player: Player = player


    def play_description(self, player: Player, current_room: Room) -> None:
        for description in current_room.description:
            click.secho(description, fg='bright_white', italic=True)
        print(*current_room.exits, sep='\n')


    def play_choice(self, player: Player, current_room: Room) -> None:
        if len(current_room.choice) > 1:
            input.get_valid_choice(player, current_room)


    def play_scene(self, player: Player, current_room: Room) -> None:
        self.play_description(player, current_room)
        self.play_choice(player, current_room)
        input.get_valid_input(player, current_room, manager)


    def update_location(self, exit: str) -> None:
        click.secho(f"(manager.py) Updating MANAGER.location to: {exit}", fg='red')
        self.location = rooms[exit]
        self.items = self.location.items
        click.secho(f"(manager.py) MANAGER.location successfully updated to: {exit}", fg='red')
    

    def update_items(self, current_room: Room, item: str, player, action: str) -> None:
        if action == "take":
            player.add_item(current_room, item)
            self.items.pop(item)

            print(f"Player items:\n{player.items}")
            print(f"Room items:\n{current_room.items}")

        elif action == "drop":
            self.items[item] = player.drop_item(current_room, item)
            
            print(f"Player items:\n{player.items}")
            print(f"Room items:\n{current_room.items}")
            
manager: Manager = Manager()