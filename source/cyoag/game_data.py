from typing import Dict, Optional

from cyoag.data_loader import DataLoader
from cyoag.data_types import Event, Item, MetaData, Room, Skin


class GameData:
    def __init__(self, loader: Optional[DataLoader]):
        self.loader = loader or DataLoader()
        raw = self.loader.load_data()

        self.rooms: Dict[str, Room] = raw["rooms"]
        self.events: Dict[str, Event] = raw["events"]
        self.items: Dict[str, Item] = raw["items"]
        self.skins: Dict[str, Skin] = raw["skins"]
        self.meta: MetaData = raw["meta"]

    @property
    def start_room(self) -> Room:
        return self.rooms[self.meta.start_room]

    @property
    def end(self) -> Room:
        return self.rooms[self.meta.end_room]

    @property
    def default_skin(self) -> Skin:
        return self.skins[self.meta.default_skin]

    @property
    def initial_event_key(self) -> str:
        return self.meta.initial_event
