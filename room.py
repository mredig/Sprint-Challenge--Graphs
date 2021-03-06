# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, id=0, x=None, y=None):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
    def __str__(self):
        return repr(self)
        return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.get_exits_string()}\n"
    def __repr__(self):
        connectedRooms = [x.id for x in [self.n_to, self.e_to, self.s_to, self.w_to] if x is not None]
        return f"Room {self.id}: ({self.x}, {self.y}) {connectedRooms}"
    def print_room_description(self, player):
        print(repr(self))
    def get_exits(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.w_to is not None:
            exits.append("w")
        if self.e_to is not None:
            exits.append("e")
        return exits
    def get_exits_string(self):
        return f"Exits: [{', '.join(self.get_exits())}]"
    def connect_rooms(self, direction, connecting_room):
        if direction == "n":
            self.n_to = connecting_room
            connecting_room.s_to = self
        elif direction == "s":
            self.s_to = connecting_room
            connecting_room.n_to = self
        elif direction == "e":
            self.e_to = connecting_room
            connecting_room.w_to = self
        elif direction == "w":
            self.w_to = connecting_room
            connecting_room.e_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None
    def get_room_in_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def directionOfRoom(self, room):
        if self.n_to is not None and room.id == self.n_to.id:
            return "n"
        elif self.s_to is not None and room.id == self.s_to.id:
            return "s"
        elif self.e_to is not None and room.id == self.e_to.id:
            return "e"
        elif self.w_to is not None and room.id == self.w_to.id:
            return "w"
        else:
            return None

    def allConnections(self):
        conns = {}
        if self.n_to is not None:
            conns["n"] = self.n_to
        if self.e_to is not None:
            conns["e"] = self.e_to
        if self.s_to is not None:
            conns["s"] = self.s_to
        if self.w_to is not None:
            conns["w"] = self.w_to
        return conns

    def roomsOtherThan(self, room):
        otherRooms = []
        if self.n_to is not None and room.id != self.n_to.id:
            otherRooms.append(self.n_to)
        if self.s_to is not None and room.id != self.s_to.id:
            otherRooms.append(self.s_to)
        if self.e_to is not None and room.id != self.e_to.id:
            otherRooms.append(self.e_to)
        if self.w_to is not None and room.id != self.w_to.id:
            otherRooms.append(self.w_to)
        return otherRooms

    def get_coords(self):
        return [self.x, self.y]
