import json
import logging
from pathlib import Path
from typing import Dict, Optional, Type, TypeVar

from pydantic import BaseModel

from cyoag.data_types import Event, Item, MetaData, Room, Skin

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class DataLoader:
    DATA_DIR = Path(__file__).parent / "data"

    def _load_collection(self, filename: str, model: Type[T]) -> Dict[str, T]:
        raw = json.loads((self.DATA_DIR / f"{filename}.json").read_text())
        return {obj["name"]: model(**obj) for obj in raw}

    def _load_meta(self) -> MetaData:
        raw_text = (self.DATA_DIR / "meta.json").read_text(encoding="utf8")
        return MetaData.model_validate_json(raw_text)

    def trigger_func_constructor(self, trigger_data: Dict[str, str]):
        trigger_type = trigger_data.get("type")

        if trigger_type == "room_status":
            trigger_room: Optional[str] = trigger_data.get("room")
            trigger_status: Optional[str] = trigger_data.get("status")

            if trigger_room is None or trigger_status is None:
                raise ValueError(
                    "Missing required keys in trigger_data: 'room' and 'status'"
                )

            return (
                lambda manager: manager.location.name == trigger_room
                and manager.status == trigger_status
            )

    def load_data(self) -> Dict:
        data = {
            "events": self._load_collection("events", Event),
            "items": self._load_collection("items", Item),
            "rooms": self._load_collection("rooms", Room),
            "skins": self._load_collection("skins", Skin),
            "meta": self._load_meta(),
        }

        for event in data["events"].values():
            event.trigger_func = self.trigger_func_constructor(event.trigger)

        for room in data["rooms"].values():
            room.items = {n: data["items"][n] for n in room.item_list}
            room.events = {n: data["events"][n] for n in room.event_list}

        logger.debug(data)
        return data
