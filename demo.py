from scenes import *
import json

def get_data(file):
  with open(file, 'r') as f:
    return json.load(f)

class Player:
  def __init__(self):
    self.items = []
    self.location = 0
  def update_location(self, id = int):
    print("Moving to new location!")
    self.location = id
  def update_items(self, item):
    print(f"Added {item} to inventory!")
    self.items.append(item)

# not used
class Room: 
  def __init__(self, name, id, description):
    self.name = name
    self.id
    self.description = description
    self.exits = []
    self.items = []

# not used
class Item:
  def __init__(self, name, description, is_movable):
    self.name = name
    self.description = description
    self.is_movable = is_movable

PLAYER = Player()
DATA = get_data('items.json')

def initiate():
  choice = input("Would you like to play, yes or no?")
  if choice == "no":
    input("Okay program will quit.\nPress Enter to continue...")
    exit()
  else:
    play_game()

def play_game():
  scene = scene_one(PLAYER, DATA)
  scene_two(PLAYER, DATA)

initiate()

# TODO: Random element, enemy, item, stage?
# TODO: Stage choice
# TODO: Loop? Locked in room until find key
# TODO: verbs: drop, take, examine, help
# TODO: rooms/player/item as classes