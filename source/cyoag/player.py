from typing import Dict, List
from item import Item
from rooms import Room

class Player:
    def __init__(self) -> None:
        self.items: Dict[str, Item] = {}
        self.location: str = "start"
    def add_item(self, current_room: Room, item: str) -> None:
        self.items[item] = current_room.items[item]
    def drop_item(self, current_room, item: str) -> Item:
        return self.items.pop(item)

player: Player = Player()