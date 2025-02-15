import json
import os
from typing import Dict, List

from pydantic import BaseModel

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "data", "rooms.json")


class Room(BaseModel):
    name: str
    id: int
    description: List[str]
    choice: List[str]
    # exit_choice: str
    exits: List[str]
    items: List[str]


with open(json_path, "r") as file:
    rooms_data: List[Room] = [Room(**room) for room in json.load(file)]


ROOMS: Dict[str, Room] = {room.name: room for room in rooms_data}