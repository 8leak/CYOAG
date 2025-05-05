import logging
from readchar import readkey
from typing import Optional, TYPE_CHECKING

from cyoag.data_types import Event
from cyoag.input import get_valid_choice
from rich.console import Console

if TYPE_CHECKING:
    from cyoag.manager import Manager

logger = logging.getLogger(__name__)
rich = Console()


class EventManager:
    def __init__(self, manager: "Manager"):
        self.manager = manager

    def check_and_play(self) -> None:
        logger.info("Checking if event has been triggered...")
        event = self._find_triggered_event()
        
        logger.info(f"Event: {event}")
        if event: 
            self._play(event)

    def _find_triggered_event(self) -> Optional[Event]:
        loc = self.manager.location
        if self.manager.next_event and not self.manager.next_event.played:
            return self.manager.next_event
        for event in loc.events.values():
            if event.trigger_func is None:
                continue
            if not event.trigger_func(self.manager):
                continue
            if event.played:
                continue
            return event

    def _play(self, event: Event) -> None:
        while True:
            logger.info(f"Playing event: {event.name}")
            self.manager.handle_narration(event, "narration")
            
            cmd, arg, outcome = get_valid_choice(event)

            if cmd != "invalid":
                print(f"Invalid {arg}")
                break

        self.manager.handle_narration(outcome, "narration")

        # todo: check logic, move to EventsManager? set from current_location.next_event?
        if not event.repeatable:
            event.played = True
            self.next_event = None
        elif event.next_event:
            logger.info("Setting new next_event...")
            self.manager.next_event = self.manager.location.events[event.next_event]
        else:
            self.manager.next_event = None

        # wait for input and print newline, TODO: move to narrator
        readkey()
        rich.print()
