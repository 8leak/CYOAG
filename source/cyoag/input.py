from player import Player
from rooms import Room
# from manager import MANAGER, Manager
import click

def handle_go(PLAYER: Player, current_room: Room, exit: str, MANAGER) -> bool:
    if exit not in current_room.exits:
        click.secho(f"(input.py) {exit} is not a valid exit!", fg='red')
        return False
    else:
        click.secho(f"(input.py) {exit} is a valid exit.", fg='red')
        MANAGER.update_location(exit)
        return True
    
def handle_take(PLAYER: Player, current_room: Room, item: str, MANAGER) -> None:
    if item not in current_room.items:
        click.secho(f"(input.py) {item} is not a valid item...", fg='red')
    else:
        click.secho(f"(input.py) {item} is a valid item...", fg='red')
        click.secho(f"You take the {item}!", fg='green')
        MANAGER.update_items(item, PLAYER)

def handle_inspect(PLAYER: Player, current_room: Room, item: str) -> None:
    if item not in current_room.items and item not in PLAYER.items:
        click.secho(f"(input.py) {item} is not a valid item...", fg='red')
    else:
        click.secho(f"(input.py) {item} is a valid item...", fg='red')
        click.secho(f"You inspect the {item}!", fg='green')
        print(PLAYER.items[item])

def handle_drop(PLAYER: Player, current_room: Room, item: str, MANAGER) -> None:
    if item not in PLAYER.items:
        click.secho(f"(input.py) {item} is not a valid item...", fg='red')
    else:
        click.secho(f"(input.py) {item} is a valid item...", fg='red')
        click.secho(f"You drop the {item}!", fg='green')
        current_room.items.update({item: PLAYER.items[item]})
        PLAYER.items.pop(item)

def get_valid_input(PLAYER: Player, current_room: Room, MANAGER) -> None:
    while True:
        user_input: str = click.prompt(click.style("What do you want to do?\n", fg='green'))
        inputs: list[str] = user_input.split(" ")

        if inputs[0] not in ("take", "inspect", "go", "drop"):
            print("Invalid command. Please use 'take', 'inspect', 'go', or 'drop'.\nTake and inspect not fully implemented.")
            continue

        if len(inputs) < 2:
            print(f"Missing argument. The {inputs[0]} command requires an argument.")
            continue

        command, argument = inputs[0], inputs[1]

        if command == "take":
            handle_take(PLAYER, current_room, argument, MANAGER)
        elif command == "inspect":
            handle_inspect(PLAYER, current_room, argument)
        elif command == "go":
            if handle_go(PLAYER, current_room, argument, MANAGER):
                break
        elif command == "drop":
            handle_drop(PLAYER, current_room, argument, MANAGER)


def get_valid_choice(PLAYER: Player, current_room: Room) -> None:
    while True:
        user_input: str = click.prompt(click.style("choice?", fg='green'))
        if user_input not in current_room.choice:
            print("Invalid choice. Try again..")
            continue
        else:
            print(f"You've got the {user_input}")
            break