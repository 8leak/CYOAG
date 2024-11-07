def is_valid_choice(user_input):
    return user_input in ("1", "2", "3")


def scene_one(PLAYER, DATA):
   input("You started the game yeet!\nPress Enter to continue...")
   print("You stumble through the long grass, across the open field, the sunbaked scrub whipping at your bloodied legs.")
   print("Something clanks metallically on your hip. Ripping it from your belt, you peer at it, struggling to focus your eyes in the gloom.")
   dialogue_1 = """It is...
                     [1] ...the blackiron twist blade you lifted from the sellsword in the tavern?
                     [2] ...a silver timepiece?
                     [3] ...a string of rusted prayer beads?
                     """
 
   condition = True
   while condition: 

      user_input = input(dialogue_1) 
      
      if not is_valid_choice(user_input): 
         print("Please enter a number between 1 and 3.") 
      else: 
         condition = False
         PLAYER.update_items(DATA["items"]["personalItems"][user_input])
         print(f"You fall to one knee, turning the {PLAYER.items[0]} over in your hands.")

def scene_two(PLAYER, DATA):
   print(f"Welcome to scene two, in your inventory you have {PLAYER.items[0]}")

def scene_three(PLAYER, DATA):
   print("and thats it")