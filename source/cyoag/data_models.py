# pyright: standard

from typing import TYPE_CHECKING, Callable, Dict, List, Optional
from enum import Enum

if TYPE_CHECKING:
    from cyoag.manager import Manager

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
    trigger_func: Optional[Callable[["Manager"], bool]] = None
    next_event: Optional[str]
    repeatable: bool
    played: bool = False
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

class Command(Enum):
    GO = "go"
    TAKE = "take"
    EXAMINE = "examine"
    DROP = "drop"
    INVENTORY = "inventory"
    HELP = "help"