from typing import Dict, List, Optional, Callable

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


class Event(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    name: str
    id: int
    trigger: Dict[str, str]
    trigger_func: Optional[Callable] = None
    repeatable: bool
    played: bool
    description: List[str]
    outcomes: Dict[str, Outcome]


class Room(BaseModel):
    name: str
    id: int
    description: List[str]
    exits: List[str]
    item_list: List[str]
    items: Dict[str, Item]
    event_list: List[str]
    events: Dict[str, Event]
