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
        # get_valid_input(PLAYER, current_room)
    
    # def handle_input(self, command, argument):
    #     if command == "go":
    #         print("i be goin")

    #         if argument not in MANAGER.location.exits:
    #             print("def handle_input: Location not available!")
    #         else:
    #             print("def handle_input: it worked!")
    #             PLAYER.update_location(argument)
 

    def update_location(self, exit) -> None:
        if exit not in MANAGER.location.exits:
            print("(manager.py) I cannot find that exit!")
        else:
            print(f"(manager.py) Found room: {exit}")
            MANAGER.location = ROOMS[exit]


MANAGER: Manager = Manager()