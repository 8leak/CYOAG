from player import Player
from rooms import Room
import click

def handle_go(player: Player, current_room: Room, exit: str, manager) -> bool:
    if exit not in current_room.exits:
        click.secho(f"(input.py) {exit} is not a valid exit!", fg='red')
        return False
    else:
        click.secho(f"(input.py) {exit} is a valid exit.", fg='red')
        manager.update_location(exit)
        return True
    
def handle_take(player: Player, current_room: Room, item: str, manager) -> None:
    if item not in current_room.items:
        click.secho(f"(input.py) {item} is not a valid item...", fg='red')
    else:
        click.secho(f"(input.py) {item} is a valid item...", fg='red')
        click.secho(f"You take the {item}!", fg='green')
        manager.update_items(current_room, item, player, "take")

def handle_inspect(player: Player, current_room: Room, item: str) -> None:
    if item not in current_room.items and item not in player.items:
        click.secho(f"(input.py) {item} is not a valid item...", fg='red')
    else:
        click.secho(f"(input.py) {item} is a valid item...", fg='red')
        click.secho(f"You inspect the {item}!", fg='green')
        print(player.items[item])

def handle_drop(player: Player, current_room: Room, item: str, manager) -> None:
    if item not in player.items:
        click.secho(f"(input.py) {item} is not a valid item...", fg='red')
    else:
        click.secho(f"(input.py) {item} is a valid item...", fg='red')
        click.secho(f"You drop the {item}!", fg='green')
        manager.update_items(current_room, item, player, "drop")

def get_valid_input(player: Player, current_room: Room, manager) -> None:
    print(current_room.items["ring"])
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
            handle_take(player, current_room, argument, manager)
        elif command == "inspect":
            handle_inspect(player, current_room, argument)
        elif command == "go":
            if handle_go(player, current_room, argument, manager):
                break
        elif command == "drop":
            handle_drop(player, current_room, argument, manager)


def get_valid_choice(player: Player, current_room: Room) -> None:
    while True:
        user_input: str = click.prompt(click.style("choice?", fg='green'))
        if user_input not in current_room.choice:
            print("Invalid choice. Try again..")
            continue
        else:
            print(f"You've got the {user_input}")
            break