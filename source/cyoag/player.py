# pyright: strict

from typing import Dict

from cyoag.data_models import Item, Room


class Player:
    def __init__(self) -> None:
        self.items: Dict[str, Item] = {}
        self.location: str = "start"

    def add_item(self, current_room: Room, item: str) -> None:
        self.items[item] = current_room.items[item]

    def drop_item(self, item: str) -> Item:
        return self.items.pop(item)
