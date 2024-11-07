def is_valid_choice(user_input):
    return user_input in ("1", "2", "3", "4")


def scene_one(PLAYER, DATA):
   input("You started the game yeet!\nPress Enter to continue...")
   print("You stumble through the long grass, across the open field, the sunbaked scrub whipping at your bloodied legs.")
   print("Something clanks metallically on your hip. Ripping it from your belt, you peer at it, struggling to focus your eyes in the gloom.")
   choice_1 = """It is...
                     [1] ...the blackiron twist blade you lifted from the sellsword in the tavern?
                     [2] ...a silver timepiece?
                     [3] ...a string of rusted prayer beads?
                     """
 
   condition = True
   while condition: 
      user_input = input(choice_1) 
      
      if not is_valid_choice(user_input): 
         print("Please enter a number between 1 and 3.") 
      else: 
         condition = False
         PLAYER.update_items(DATA["items"]["personalItems"][user_input])
         print(f"You fall to one knee, turning the {PLAYER.items[0]} over in your hands.")
   
   choice_2 = "Where do you go?\n[1] Dungeon\n[2] Wizard tower\n[3] Caravan\n"

   condition = True
   while condition: 
      user_input = input(choice_2) 
      
      if not is_valid_choice(user_input): 
         print("Please enter a number between 1 and 3.") 
      else: 
         condition = False
         PLAYER.location = user_input

def scene_two(PLAYER, DATA):
   print(f"Welcome to scene two, in your inventory you have {PLAYER.items[0]}")

def scene_three(PLAYER, DATA):
   print("and thats it")

def play_scene(PLAYER, DATA, current_room):
   current_room.get_description()