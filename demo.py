from items import personalItems
from scenes import *

class Inventory:
  def __init__(self):
    self.personalItem = ""
    self.badMemory = ""
    self.endGoal = ""
    self.gameStage = 1
  def asdasd():
    pass

PLAYER = Inventory()

def initiate():
  choice = input("Would you like to play, yes or no?")
  if choice == "no":
    input("Okay program will quit.\nPress Enter to continue...")
    exit()
  else:
    play_game()

def play_game():
  scene_one(PLAYER)
  print(PLAYER.personalItem)
  scene_two(PLAYER)
  print(PLAYER.personalItem)

initiate()

# TODO: Random element, enemy, item, stage?
# TODO: Stage choice
# TODO: Loop? Locked in room until find key
