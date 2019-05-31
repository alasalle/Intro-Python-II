# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
            self.name = name
            self.description = description
            self.n_to = "null"
            self.s_to = "null"
            self.e_to = "null"
            self.w_to = "null"
            self.items = items
