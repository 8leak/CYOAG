from source.cyoag.rooms import ROOMS


class Player:
    def __init__(self):
        self.items = []
        self.location = 0

    def update_location(self, current_room, exit):
        room = next((room for room in ROOMS if room.name == exit), None)

        if room:
            print(f"Found room: {room.name}")
            PLAYER.location = int(room.id)
        else:
            print("Room not found")


PLAYER = Player()
