from typing import List

from rooms import ROOMS, Room


class Player:
    def __init__(self) -> None:
        self.items: List[str] = []
        self.location: str = "start"
    # updateItems()

PLAYER: Player = Player()