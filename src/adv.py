from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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


def move(direction):
    player.move("".join(direction[0])[0])


def say(saying):
    print(f'You said {" ".join(saying)}')


action_dict = {"say": say, "move": move}


def get_input():
    action = input("What are you going to do: ").split(" ")
    verb = action[0]
    if verb in action_dict:
        command = action_dict[verb]
    else:
        print("Unknown Command {verb}")
        return
    print(command)
    if len(action) >= 2:
        noun = action[1:]
        command(noun)


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
    (playing := True if response == "y" else False)
    while playing:
        get_description()
        get_input()


main_game()
