from typing import Dict, List

from pydantic import BaseModel, ConfigDict


class Item(BaseModel):
    name: str
    id: int
    description: List[str]


class Outcome(BaseModel):
    name: str
    description: List[str]
    command: str
    argument: str


class Choice(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    name: str
    id: int
    description: List[str]
    outcomes: Dict[str, Outcome]


class Room(BaseModel):
    name: str
    id: int
    description: List[str]
    exits: List[str]
    item_list: List[str]
    items: Dict[str, Item]
    choice_list: List[str]
    choices: Dict[str, Choice]
