from player import PLAYER, Player
from rooms import ROOMS, Room
from typing import List
import click

class Manager:
    def __init__(self) -> None:
        self.items: List[str] = []
        self.location: Room = ROOMS["start"]
        self.player: Player = PLAYER
    
    def play_scene(self, PLAYER: Player, current_room: Room) -> None:
        for description in current_room.description:
            click.secho(description, fg='bright_white', italic=True)
        print(*current_room.exits, sep='\n')

    # print_descr
    # print/play_choice (if not empty)
    # print_exits

    def update_location(self, exit) -> None:
        click.secho(f"(manager.py) Updating MANAGER.location to: {exit}", fg='red')
        
        MANAGER.location = ROOMS[exit]
        
        click.secho(f"(manager.py) MANAGER.location successfully updated to: {exit}", fg='red')

MANAGER: Manager = Manager()

# create click templates
# add stubs for other verbs
# add exit choice description