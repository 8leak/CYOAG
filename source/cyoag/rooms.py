import json
import os
from typing import List

from pydantic import BaseModel

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "data", "rooms.json")


with open(json_path, "r") as file:
    rooms_data: List[dict] = json.load(file)


class Room(BaseModel):
    name: str
    id: int
    description: List[str]
    choice: str
    exit_choice: str
    exits: List[str]


ROOMS: List[Room] = [Room(**room) for room in rooms_data]

# for room in ROOMS:
#     print(f"Room: {room.name}, ID: {room.id}, Exits: {room.exits}, Descriptions: {room.description[0]}")
