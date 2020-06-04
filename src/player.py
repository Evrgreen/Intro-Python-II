# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move(self, direction):
        if f'{direction}_to' in dir(self.location):
            move_to = getattr(self.location, f'{direction}_to')
            self.location = move_to
          
