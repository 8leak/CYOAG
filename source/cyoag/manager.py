from player import PLAYER, Player
from rooms import ROOMS, Room
from typing import List

class Manager:
    def __init__(self) -> None:
        self.items: List[str] = []
        self.location: Room = ROOMS["start"]
        self.player: Player = PLAYER
    
    def play_scene(self, PLAYER: Player, current_room: Room) -> None:
        for description in current_room.description:
            print(description)
        print("Where do you want to go?")
        print(*current_room.exits, sep='\n')

    def update_location(self, exit) -> None:
        print(f"(manager.py) Updating MANAGER.location to: {exit}")
        
        MANAGER.location = ROOMS[exit]
        
        print(f"(manager.py) MANAGER.location successfully updated to: {exit}")

MANAGER: Manager = Manager()