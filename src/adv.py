from room import Room
from player import Player
from item import Item
# Declare all the rooms


class Game:
    def __init__(self, name, rooms, player):
        self.name = name
        self.rooms = rooms
        self.player = player

    def __str__(self):
        output = f'<---{self.name}--->\n\n'
        output += f'Welcome, {self.player.name}.\n'
        output += 'Where will you go?\n'
        output += 'What will you do?\n'
        output += 'Your choices are to enter N, S, E, or W.\n'
        output += 'Press Q to quit'
        return output

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.",
                     [Item("lamp", "it emits a faint glow."),
                      Item("hat", "a weather-beaten miner's hat")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [Item("tome", """an ancient moth-eaten text.
                      It's aura is strong, and somehow sacred"""),
                      Item("bust", """a marble statuette of a
                       beautiful person of indeterminate gender.""")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [Item("rope", "An eerily new rope. Who's could it be?"),
                      Item("rock", """a dusty pebble.
                       It feels solid and oddly lucky.""")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [Item("pickaxe", """it sports a worn handle.
                      And what's this...? Blood on the blade...."""),
                      Item("molar", "a black-speckled tooth.")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [Item("sceptre", "it beckons to you."),
                      Item("ruby", """beautiful and pristine
                       - and OBSCENELY large""")]),
}


# Link rooms together

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

# Make a new player object that is currently in the 'outside' room.
player = Player("Maria", room["outside"], [Item("matchbook", """might be a
little too soggy.""")])
directions = ['n', 's', 'e', 'w']

my_game = Game("Magic Kingdom", room, player)
print(my_game)
# Write a loop that:
# * Prints the current room name

while True:
        print(f'\n\nYou are in the {my_game.player.current_room.name}.')
# * Prints the current description (the textwrap module might be useful here).
        print(f'{my_game.player.current_room.description}')
# * Waits for user input and decides what to do.
        inp = input().lower().split(" ")
        verb = inp[0]
        if len(inp) == 2:
            choice = inp[1]
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

        if verb == "q":
            print("Thanks for playing!")
            exit()
        elif verb == "go":
            if choice in directions:
                my_game.player.travel(choice)
            else:
                print("Not a valid direction. Your choices are N, S, E, or W.")
        elif verb == "get" or verb == "take":
            for item in my_game.player.current_room.items:
                if item.name == choice:
                    my_game.player.take(item)
                #     my_game.room.remove(item.name)
                #     item.on_take()
                elif choice != my_game.player.current_room.items[len(my_game.player.current_room.items) - 1].name:
                    print("There is no such item in this room.")
        elif verb == "drop":
            for item in my_game.player.items:
                if item.name == choice:
                    my_game.player.drop(item.name)
                #     my_game.room.add(item)
                #     item.on_drop()
                elif choice != my_game.player.items[len(my_game.player.items) - 1].name:
                    print("There is no such item in your inventory.")
        elif verb == "i" or verb == "inventory":
            items_list = []
            print("Here are all of the items you are carrying:\n")
            for item in my_game.player.items:
                print(f"""{item.name}:\n{item.description}\n""")
        else:
                print("Not a valid command or directions")
