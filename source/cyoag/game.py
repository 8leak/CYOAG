from player import PLAYER
from rooms import ROOMS
from manager import MANAGER, Manager
from input import get_valid_input


def initiate() -> None:
    choice: str = input("Would you like to play, yes or no?\n> ")
    if choice == "no":
        input("Press any button to quit.")
        exit()
    else:
        play_game()


def play_game() -> None:
    game_running: bool = True

    while game_running:
        current_room = MANAGER.location
        print(f"(game.py) Set current location to: {current_room.name}")
        
        if current_room.name == "shrine":
            game_running = False
            print("(game.py) I should be quitting!")
        else:
            MANAGER.play_scene(PLAYER, current_room)
            get_valid_input(PLAYER, current_room)

    print("(game.py) YOU DIED")


initiate()

# TODO: Random element, enemy, item, stage?
# TODO: Loop? Locked in room until find key
# TODO: rebuild 'choice' as just what would you like to do? > inspect door > go dungeon > help > take key
