# Implement a class to hold room information. This should have name and
# description attributes.

from store import Store


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = Store({})

    def __str__(self):
        return f"{self.name}, {self.description}"

    def search(self):
        if len(self.items) > 0:
            return f'You look around and discover {self.items}'
        else:
            f'The room appears to be empty'
