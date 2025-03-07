import json
import os
from typing import Dict, List

from item import Item, items
from pydantic import BaseModel

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "data", "rooms.json")


class Room(BaseModel):
    name: str
    id: int
    description: List[str]
    choice: List[str]
    exits: List[str]
    item_list: List[str]
    items: Dict[str, Item]


with open(json_path, "r") as file:
    rooms_data: List[Room] = [Room(**room) for room in json.load(file)]


rooms: Dict[str, Room] = {room.name: room for room in rooms_data}
for room in rooms.values():
    room.items = {item: items[item] for item in room.item_list}
