import logging
from typing import Optional, Tuple

from cyoag.data_types import Callable, Command, Dict

logger = logging.getLogger(__name__)


class CommandProcessor:
    def __init__(self, manager):
        self.manager = manager
        self.command_map: Dict[
            Command, Tuple[Callable[[Optional[str]], bool], bool]
        ] = {
            Command.TAKE: (self.manager.handle_take, True),
            Command.EXAMINE: (self.manager.handle_examine, False),
            Command.GO: (self.manager.handle_go, True),
            Command.DROP: (self.manager.handle_drop, True),
            Command.INVENTORY: (self.manager.handle_inventory, False),
            Command.HELP: (self.manager.handle_help, False),
        }

    def handle(self, cmd: Command, arg: Optional[str]):
        handler, needs_arg = self.command_map[cmd]

        if needs_arg:
            if (arg := self._ensure_arg(cmd.value, arg)) is None:
                return False
        return handler(arg or None)

    def _ensure_arg(self, cmd_name: str, arg: Optional[str]) -> Optional[str]:
        if not arg:
            self.manager.handle_narration(
                f"{cmd_name} requires an argument.", "action"
            )
            return None
        return arg
