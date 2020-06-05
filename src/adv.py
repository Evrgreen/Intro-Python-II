from room import Room
from player import Player
import item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
room['outside'].items.add_to_store(
    item.Item("Gold", "The Currency of the Capital", 100))
room['treasure'].items.add_to_store(
    item.Item("Gold", "The Currency of the Capital", 1000))
room['foyer'].items.add_to_store(item.Dagger())
room['overlook'].items.add_to_store(item.Sword())


print('n' in "nsew")


def move(direction):
    player.move("".join(direction[0]))


def say(saying):
    print(f'You said {" ".join(saying)}')


def search():
    print(player.location.search())


def quit():
    player.playing = False


def check():
    print(player.check_inventory())


def pickup(item):
    if item[0] in player.location.items:
        item_to_pickup = player.location.items.remove_from_store(item[0])
        player.inventory.add_to_store(item_to_pickup)


def drop(item):
    if item[0] in player.inventory:
        item_to_drop = player.inventory.remove_from_store(item[0])
        player.location.items.add_to_store(item_to_drop)
        print(f'You dropped {item_to_drop.name}')


def examine(object):
    if object[0] in player.inventory:
        print(player.inventory.items[object[0]])
    else:
        print("Cannot Locate that Item")


action_dict = {"say": say, "move": move, "search": search,
               "q": quit, "pickup": pickup, "examine": examine, "check": check, "drop": drop}


def get_input():
    action = input("What are you going to do: ").split(" ")
    verb = action[0]
    if verb in action_dict:
        command = action_dict[verb]
    else:
        print("Unknown Command {verb}")
        return
    if len(action) >= 2:
        noun = action[1:]
        command(noun)
    else:
        return command()


player = Player("Stanley", room['outside'])


def get_description():
    print(f" \n {player.location}  \n")
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# While True
def main_game():
    print(f"Welcome to Generic Fantasy Game")
    response = input(f"Begin Game? Y/N:  ").lower()
    player.playing = True if response == "y" else False
    while player.playing:
        get_description()
        get_input()


main_game()
