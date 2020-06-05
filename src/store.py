class Store:
    def __init__(self, items):
        self.items = items

    def add_to_store(self, item):
        self.items[item.name] = item

    def remove_from_store(self, item):
        return self.items.pop(item)

    def __len__(self):
        return len(self.items.keys())

    def __str__(self):
        return f'{" ".join([item for item in self.items.keys()])}'

    def __contains__(self, other):
        return True if other in self.items.keys() else False
