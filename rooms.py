import json
from pydantic import BaseModel
from typing import List, Dict

with open('rooms.json', 'r') as file:
    rooms_data = json.load(file)

class Room(BaseModel):
    name: str
    id: str
    description: List[str]
    choice: str
    exit_choice: str
    exits: List[str]

ROOMS = [Room(**room) for room in rooms_data]

# for room in ROOMS:
#     print(f"Room: {room.name}, ID: {room.id}, Exits: {room.exits}, Descriptions: {room.description[0]}")