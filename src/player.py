# Write a class to hold player information, e.g. what room they are in
# currently.

from store import Store
import item


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.playing = False
        self.inventory = Store({})

    def move(self, direction):
        if (f'{direction[0]}_to') in dir(self.location):
            move_to = getattr(self.location, f'{direction[0]}_to')
            self.location = move_to
        else:
            print(f'There is no exit to the {direction.capitalize}')

    def check_inventory(self):
        if len(self.inventory) > 0:
            return f'You are carrying {self.inventory}'
        else:
            return f'Your inventory is empty'
