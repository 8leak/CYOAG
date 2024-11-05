from items import personalItems

def scene_one(PLAYER):
   input("You started the game yeet!\nPress Enter to continue...")
   print("You stumble through the long grass, across the open field, the sunbaked scrub whipping at your bloodied legs.")
   print("Something clanks metallically on your hip. Ripping it from your belt, you peer at it, struggling to focus your eyes in the gloom.")
   personalItem = input("""It is...
                     [1] ...the blackiron twist blade you lifted from the sellsword in the tavern?
                     [2] ...a silver timepiece?
                     [3] ...a string of rusted prayer beads?
                     """)
   PLAYER.personalItem = personalItems[int(personalItem) - 1]
   print(f"You fall to one knee, turning the {PLAYER.personalItem} over in your hands.")

def scene_two(PLAYER):
   print("and now we slappin")

def scene_three(PLAYER):
   print("and thats it")