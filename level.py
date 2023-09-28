from pick import pick
from os import system
from Room.Cave import Cave
from Classes.index import Player


class formats:
    Bold = "\x1b[1m"
    Dim = "\x1b[2m"
    Italic = "\x1b[3m"
    Underlined = "\x1b[4m"
    Blink = "\x1b[5m"
    Reverse = "\x1b[7m"
    Hidden = "\x1b[8m"
    # Reset part
    Reset = "\x1b[0m"
    Reset_Bold = "\x1b[21m"
    Reset_Dim = "\x1b[22m"
    Reset_Italic = "\x1b[23m"
    Reset_Underlined = "\x1b[24"
    Reset_Blink = "\x1b[25m"
    Reset_Reverse = "\x1b[27m"
    Reset_Hidden = "\x1b[28m"


class Level:
    def __init__(self, rooms, player, defx=0, defy=0):
        self.rooms = rooms
        self.player = player
        self.defy = defy
        self.defx = defx

    def pick_room(self):
        choices = []
        self.player.xpos, self.player.ypos = self.defx, self.defy
        for room in self.rooms:
            choices.append(room.name)
        option, index = pick(choices, "Velg et rom",
                             indicator='=>', default_index=0)
        self.set_scene(index)

    def set_scene(self, room_index):
        self.current_room = self.rooms[room_index]

    def draw_room(self):
        system("cls")
        room_fill = [""]

        # Bold
        print(formats.Bold + self.current_room.name + formats.Reset)
        print(formats.Italic + self.current_room.description + formats.Reset_Italic)

        for y in range(0, self.current_room.size_y):
            for x in range(0, self.current_room.size_x):
                if x == self.player.xpos and y == self.player.ypos:
                    room_fill.append(self.player.apperance)
                else:
                    room_fill.append(self.current_room.empty_material)

        i = 1
        for y in range(0, self.current_room.size_y):
            if (y == 0):
                for x in range(0, self.current_room.size_x+2):
                    print(self.current_room.material, end="")
                print("")
            for x in range(0, self.current_room.size_x):
                if x == 0:
                    print(self.current_room.material, end="")

                print(room_fill[i], end="")
                if x == self.current_room.size_x-1:
                    print(self.current_room.material, end="")
                i += 1

            print("")
            tekst = ""
            if y == self.current_room.size_y-1:
                for x in range(0, self.current_room.size_x+2):
                    tekst += self.current_room.material
                tekst += "\n"
            print(tekst, end="")
        input("Press Enter for å se valg. ")

    def draw_room_with_choices(self, additional_choices):
        self.draw_room()

        choices = []
        if (self.player.ypos != 0):
            choices.append("Opp")
        if (self.player.ypos != self.current_room.size_y-1):
            choices.append("Ned")
        if (self.player.xpos != 0):
            choices.append("Venstre")

        if (self.player.xpos != self.current_room.size_x-1):
            choices.append("Høyre")

        option, index = pick([*choices, *additional_choices.keys(), "Se brettet"],
                             "Velg hva du vil gjøre", indicator='=>', default_index=0, )

        if (option in additional_choices.keys()):
            additional_choices[option]()

        if (option == "Se brettet"):
            self.draw_room_with_choices(additional_choices)

        if (option == "Opp"):
            self.player.ypos = self.player.ypos - \
                self.player.speed if (
                    self.player.ypos - self.player.speed > 0) else 0

            self.draw_room_with_choices(additional_choices)

        if (option == "Ned"):
            self.player.ypos = self.player.ypos + \
                self.player.speed if (self.player.ypos - self.player.speed <
                                      self.current_room.size_y-1) else self.current_room.size_y-1
            self.draw_room_with_choices(additional_choices)

        if (option == "Venstre"):
            self.player.xpos = self.player.xpos - \
                self.player.speed if (
                    self.player.xpos - self.player.speed > 0) else 0

            self.draw_room_with_choices(additional_choices)

        if (option == "Høyre"):
            self.player.xpos = self.player.xpos + \
                self.player.speed if (self.player.xpos < self.current_room.size_x -
                                      1) else self.current_room.size_x-1

            self.draw_room_with_choices(additional_choices)
