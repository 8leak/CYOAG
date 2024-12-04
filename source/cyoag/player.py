from typing import List

from rooms import ROOMS, Room


class Player:
    def __init__(self) -> None:
        self.items: List[str] = []
        self.location: int = 0

    def update_location(self, current_room: Room, exit: str) -> None:
        room = next((room for room in ROOMS if room.name == exit), None)

        if room:
            print(f"Found room: {room.name}")
            PLAYER.location = room.id
        else:
            print("Room not found")


PLAYER: Player = Player()
