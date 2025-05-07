# pyright: standard

from enum import Enum
from typing import TYPE_CHECKING, Callable, Dict, List, Optional

if TYPE_CHECKING:
    from cyoag.manager import Manager

from pydantic import BaseModel, Field


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
    # model_config = ConfigDict(arbitrary_types_allowed=True)
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
    items: Dict[str, Item] = Field(default_factory=dict)
    event_list: List[str]
    events: Dict[str, Event] = Field(default_factory=dict)


class Command(Enum):
    GO = "go"
    TAKE = "take"
    EXAMINE = "examine"
    DROP = "drop"
    INVENTORY = "inventory"
    HELP = "help"


class Skin(BaseModel):
    name: str
    info: str
    warning: str
    danger: str
    narration: str
    action: str
    choice: str
    title: str


class MetaData(BaseModel):
    start_room: str
    end_room: str
    default_skin: str
    initial_event: str
