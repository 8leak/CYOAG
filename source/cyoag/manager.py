from player import PLAYER, Player
from rooms import ROOMS, Room
from typing import List
import input
import click

class Manager:
    def __init__(self) -> None:
        self.location: Room = ROOMS["start"]
        self.items: List[str] = self.location.items
        self.player: Player = PLAYER
    
    def play_description(self, PLAYER: Player, current_room: Room) -> None:
        for description in current_room.description:
            click.secho(description, fg='bright_white', italic=True)
        print(*current_room.exits, sep='\n')

    def play_choice(self, PLAYER: Player, current_room: Room) -> None:
        if len(current_room.choice) > 1:
            input.get_valid_choice(PLAYER, current_room)

    def play_scene(self, PLAYER: Player, current_room: Room) -> None:
        self.play_description(PLAYER, current_room)
        self.play_choice(PLAYER, current_room)
        input.get_valid_input(PLAYER, current_room, MANAGER)

    def update_location(self, exit: str) -> None:
        click.secho(f"(manager.py) Updating MANAGER.location to: {exit}", fg='red')
        self.location = ROOMS[exit]
        self.items = self.location.items
        click.secho(f"(manager.py) MANAGER.location successfully updated to: {exit}", fg='red')
    
    def update_items(self, item: str, PLAYER) -> None:
        PLAYER.items.update({item: self.items[item]})
        click.secho(PLAYER.items[item], fg='bright_white', italic=True)

        self.items.pop(item)

        print("\nInventory:", *PLAYER.items, sep='\n')
        print("\nRemaining items:", *self.items, sep='\n')

MANAGER: Manager = Manager()

# create click templates
# add exit choice description