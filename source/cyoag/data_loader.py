from typing import Dict, Optional
from pathlib import Path
from cyoag.data_models import Event, Item, Room
import json


class DataLoader:
    def __init__(self) -> None:
          pass

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
        current_dir = Path(__file__).resolve().parent
        json_path = current_dir / "data"
        data_dicts = {}
        data_map = {"events": Event, "items": Item, "rooms": Room}

        for filename, class_type in data_map.items():
            with open(json_path / f"{filename}.json", "r") as file:
                data = [class_type(**items) for items in json.load(file)]
                data_dicts.update(
                    {filename: {item.name: item for item in data}}
                )

        for event in data_dicts["events"].values():
            event.trigger_func = self.trigger_func_constructor(event.trigger)

        for room in data_dicts["rooms"].values():
            room.items = {
                item: data_dicts["items"][item] for item in room.item_list
            }
            room.events = {
                event: data_dicts["events"][event] for event in room.event_list
            }

        return data_dicts