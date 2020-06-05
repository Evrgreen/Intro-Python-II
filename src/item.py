import random


class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

        def __str__(self):
            spacing = "="*20
            return f'{spacing}\n {self.name} \n {spacing}\n {self.description}'


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage

        super().__init__(name, description, value)

        def __str__(self):
            spacing = "="*20
            return f'{spacing}\n {self.name}  Damage: {self.damage}\n {spacing}\n {self.description}'


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=2,)


class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A noble blade capable of.....ouch did you just cut your finger?",
                         value=10,
                         damage=2,)


adjective = {"Rusty": {"name": "Rusty", "description": "Probably the World's rustiest",
                       "damage": "2"}, "Silver": {"name": "Silver", "description": "The Ultimate", "damage": "5"}}
noun = {"Dagger": {"name": "Dagger", "is_class": "Weapon", "description": "Dagger", "value": 10},
        "Sword": {"name": "Sword", "is_class": "Weapon", "description": "Sword", "value": 100}}


def Merge(dic1, dic2):
    dic1, dic2 = dic1, dic2
    res = {x: f"{dic1.get(x, '')} {dic2.get(x, '')}"
           for x in set(dic1).union(dic2)}
    return res


newItem = []
for num in range(1, random.randint(1, 10)):
    newItem.append(Merge(random.choice(list(adjective.values())),
                         random.choice(list(noun.values()))))
