from player import PLAYER, Player
from rooms import ROOMS, Room
from scenes import get_valid_input, play_scene


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
        current_room = ROOMS[PLAYER.location]

        if current_room.id == 4:
            game_running = False
            print("I should be quitting!")
        else:
            play_scene(PLAYER, current_room)

    print("Game over!")


initiate()

# TODO: Random element, enemy, item, stage?
# TODO: Loop? Locked in room until find key
# TODO: rebuild 'choice' as just what would you like to do? > inspect door > go dungeon > help > take key
