from rich.theme import Theme
from rich.console import Console


theme_1 = Theme(
    {
        "info": "dim cyan",
        "warning": "bold",
        "danger": "bold red",
        "narration": "italic bright_white",
        "action": "bold",
        "choice": "bold green",
        "title": "bold italic bright_white"
    }
)

class Narrator:
    def __init__(self, theme=Theme) -> None:
        self.theme: Theme = theme
        self.console: Console = Console(theme=theme_1)
    def say(self, txt, style):
        self.console.print(txt, style=style, markup=False, highlight=False)