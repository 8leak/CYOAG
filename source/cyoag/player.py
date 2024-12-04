from typing import List

from rooms import ROOMS, Room


class Player:
    def __init__(self) -> None:
        self.items: List[str] = []
        self.location: str = "start"

    def update_location(self, current_room: Room, exit: str) -> None:
        if exit not in current_room.exits:
            print("I cannot find that exit!")
        else:
            print(f"Found room: {exit}")
            PLAYER.location = exit


PLAYER: Player = Player()