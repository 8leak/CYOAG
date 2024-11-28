from scenes import *
import json

def get_data(file):
  with open(file, 'r') as f:
    return json.load(f)

class Player:
  def __init__(self):
    self.items = []
    self.location = "0"

  def update_items(self, item):
    print(f"Added {item} to inventory!")
    self.items.append(item)
  
  def update_location(self, current_room, exit):
    # convert the exit dictionaries to tuple lists? 
    result = [key for key, value in current_room.exits.items() if value == exit]
    PLAYER.location = result[0]
    print(f"Moving to {ROOMS[int(PLAYER.location)].name}!")

class Room:
  # pydantic
  def __init__(self, name, id, description, choice, exit_choice, exits):
    self.name = name
    self.id = id
    self.description = description
    self.choice = choice
    self.exit_choice = exit_choice
    self.exits = exits

  def display_description(self):
    for description in self.description:
      print(description)
  
  def get_exit_names(self):
    exit_names = []
    for exit_id, exit_name in self.exits.items():
      exit_names.append(exit_name)
    return exit_names

PLAYER = Player()
DATA = get_data('items.json')
ROOMS = []
ROOMSDATA = get_data('rooms.json')

def populate_rooms():
  for room_id, room_data in ROOMSDATA.items():
    ROOMS.append(Room(
      room_data["name"],
      room_data["id"],
      room_data["description"],
      room_data["choice"],
      room_data["exit_choice"],
      room_data["exits"]))

def initiate():
  choice = input("Would you like to play, yes or no?\n")
  if choice == "no":
    input("Okay program will quit")
    exit()
  else:
    play_game()

def play_game():
  game_running = True

  while game_running:
    current_room = ROOMS[int(PLAYER.location)]

    if current_room.id == "4":
      game_running = False
      print("I should be quitting!")
    else:
      play_scene(PLAYER, DATA, current_room)

  print("Game over!")
  
populate_rooms()
initiate()

# TODO: Random element, enemy, item, stage?
# TODO: Stage choice
# TODO: Loop? Locked in room until find key
# TODO: verbs: drop, take, examine, help
# TODO: map a json library of rooms (with various attributes) into room class instances (instead of manually putting each one in as argument)
# TODO: rebuild 'choice' as just what would you like to do? > inspect door > go dungeon > help > take key