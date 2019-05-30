# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def travel(self, direction):
        if direction == "n":
            new_room = self.current_room.n_to
            if new_room != "null":
                self.current_room = new_room
            else:
                print("There's nothing that way. Pick again.")
        elif direction == "s":
            new_room = self.current_room.s_to
            if new_room != "null":
                self.current_room = new_room
            else:
                print("There's nothing that way. Pick again.")
        elif direction == "e":
            new_room = self.current_room.e_to
            if new_room != "null":
                self.current_room = new_room
            else:
                print("There's nothing that way. Pick again.")
        elif direction == "w":
            new_room = self.current_room.w_to
            if new_room != "null":
                self.current_room = new_room
            else:
                print("There's nothing that way. Pick again.")
