import json
import os
from typing import Dict, List

from pydantic import BaseModel, ConfigDict

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "data", "choices.json")

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
    outcomes: {str, Outcome}


with open(json_path, "r") as file:
    choices_data: List[Choice] = [Choice(**choices) for choices in json.load(file)]


choices: Dict[str, Choice] = {choices.name: choices for choices in choices_data}
