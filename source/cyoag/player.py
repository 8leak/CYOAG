from typing import List

from rooms import ROOMS, Room


class Player:
    def __init__(self) -> None:
        self.items: dict = {}
        self.location: str = "start"
    # updateItems()

PLAYER: Player = Player()