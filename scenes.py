def get_valid_input(PLAYER, current_room):
   while True:
      user_input = input(current_room.exit_choice)
      inputs = user_input.split(" ")

      if not inputs[0] in ("take", "inspect", "go"):
         print("Invalid command. Please use 'take', 'inspect' or 'go'.\nTake and inspect no implemented.")
         continue
      
      if len(inputs) < 2:
         print(f"Missing argument. The {inputs[0]} command requires an argument.")
         continue
      
      command, argument = inputs[0], inputs[1]

      if command == "take":
         print("takin some shit")
         # PLAYER.take(argument)
         break
      
      elif command == "inspect":
         print("inspectin some shit")
         # PLAYER.inspect(argument)
         break

      elif command == "go":
         print("i be goin")
         if argument not in current_room.exits:
            print("Location not available!")
            continue
         else:
            print("it worked!")
            PLAYER.update_location(current_room, argument)
            break

   
def play_scene(PLAYER, current_room):
   print(current_room.description[0])
   get_valid_input(PLAYER, current_room)
   print("are we alive")