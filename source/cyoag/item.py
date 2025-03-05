import json
import os
from typing import Dict, List

from pydantic import BaseModel

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "data", "items.json")


class Item(BaseModel):
    name: str
    id: int
    description: List[str]

with open(json_path, "r") as file:
    items_data: List[Item] = [Item(**items) for items in json.load(file)]


items: Dict[str, Item] = {items.name: items for items in items_data}

# choice models