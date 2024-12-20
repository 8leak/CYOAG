from player import PLAYER
from rooms import ROOMS
from scenes import play_scene


def initiate() -> None:
    choice: str = input("Would you like to play, yes or no?\n")
    if choice == "no":
        input("Okay program will quit")
        exit()
    else:
        play_game()


def play_game() -> None:
    game_running: bool = True

    while game_running:
        current_room = ROOMS[PLAYER.location]

        if current_room.name == "shrine":
            game_running = False
            print("I should be quitting!")
        else:
            play_scene(PLAYER, current_room)

    print("Game over! you win?")


initiate()

# TODO: Random element, enemy, item, stage?
# TODO: Loop? Locked in room until find key
# TODO: rebuild 'choice' as just what would you like to do? > inspect door > go dungeon > help > take key
