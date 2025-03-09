import logging
from typing import Dict, List

import click
from item import Item
from player import Player
from rooms import Room
from choice import Choice, Outcome


def handle_go(player: Player, current_room: Room, exit: str, manager) -> bool:
    if exit not in current_room.exits:
        click.secho(f"Cannot find {exit}!", fg="green")
        logging.warning(f"Player tried to go to an invalid exit: {exit}")
        return False
    else:
        logging.info(f"Player found exit: {exit}")
        manager.update_location(exit)
        return True


def handle_take(player: Player, current_room: Room, item: str, manager) -> None:
    if item not in current_room.items:
        click.secho(f"You cannot find the {item}!", fg="green")
        logging.warning(f"Player tried to take an invalid item: {item}")
    else:
        logging.info(f"Player found item: {item}")
        manager.update_items(current_room, item, player, "take")
        click.secho(f"You take the {item}!", fg="green")

        inventory_items = ", ".join(player.items.keys())
        logging.info(f"Player's inventory after taking item: {inventory_items}")


def handle_drop(player: Player, current_room: Room, item: str, manager) -> None:
    if item not in player.items:
        click.secho(f"{item} not in your inventory")
        logging.warning(f"Player tried to drop an item not in inventory: {item}")
    else:
        click.secho(f"You drop the {item}!", fg="green")
        logging.info(f"Player dropped item: {item}")
        manager.update_items(current_room, item, player, "drop")


def handle_inspect(player: Player, current_room: Room, item: str) -> None:
    if item not in current_room.items and item not in player.items:
        logging.debug(f"Player tried to inspect an invalid item: {item}")
        click.secho(f"You can't find the {item} here.", fg="green")
    elif item in player.items:
        logging.info(f"Player inspected item in inventory: {item}")
        print(player.items[item].description)
    elif item in current_room.items:
        logging.info(f"Player inspected item in room: {item}")
        print(current_room.items[item].description)


def handle_inventory(player: Player) -> List[str]:
    if len(player.items) >= 1:
        logging.info("Player checked inventory")
        print("Inventory:")
        for item in player.items:
            print(f"- {item}")
    else:
        logging.info("Player checked inventory: empty")
        print("Your inventory is empty!")


def get_valid_input(player: Player, current_room: Room, manager) -> None:
    while True:
        user_input: str = click.prompt(
            click.style("What do you want to do?\n", fg="green")
        )
        inputs: List[str] = user_input.split(" ")

        if inputs[0] not in ("take", "inspect", "go", "drop", "inventory"):
            logging.warning(f"Invalid command: {inputs[0]}")
            print(
                "Invalid command. Please use 'take', 'inspect', 'go', 'drop', or 'inventory'."
            )
            continue

        if len(inputs) < 2:
            command = inputs[0]
        else:
            command, argument = inputs[0], inputs[1]

        logging.debug(
            f"Player command: {command} {argument if len(inputs) > 1 else ''}"
        )

        handle_command(player, current_room, manager, command, argument)
        # if command == "take":
        #     handle_take(player, current_room, argument, manager)
        # elif command == "inspect":
        #     handle_inspect(player, current_room, argument)
        # elif command == "go":
        #     if handle_go(player, current_room, argument, manager):
        #         break
        # elif command == "drop":
        #     handle_drop(player, current_room, argument, manager)
        # elif command == "inventory":
        #     handle_inventory(player)


def handle_command(player, current_room, manager, command, argument):
    if command == "take":
            handle_take(player, current_room, argument, manager)
    elif command == "inspect":
        handle_inspect(player, current_room, argument)
    elif command == "go":
        if handle_go(player, current_room, argument, manager):
            pass
    elif command == "drop":
        handle_drop(player, current_room, argument, manager)
    elif command == "inventory":
        handle_inventory(player)



def get_valid_choice(player: Player, current_room: Room, manager) -> None:
    while True:
        event = current_room.choices["choice1"]
        click.secho(event.description[0], fg="bright_white", italic=True)
                
        user_input: str = click.prompt(click.style("choice?", fg="green"))
        
        if user_input not in event.outcomes:
            print("invalid choice!")
        else:
            print("valid choice!")
            outcome = event.outcomes[user_input]
            print(outcome.description[0])
            command, argument = outcome.command, outcome.argument
            handle_command(player, current_room, manager, command, argument)

            break

            #TODO: choice handling, room memory, room mechanics
