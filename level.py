from pick import pick
from os import system
from Room.Cave import Cave

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
    def __init__(self, rooms, player):
        self.rooms = rooms
        self.player = player
    
    def pick_room(self):
        choices = []
        for room in self.rooms:
            choices.append(room.name)
        option, index = pick(choices, "Velg et rom", indicator='=>', default_index=0)
        self.set_scene(index)

    def set_scene(self, room_index):
        self.current_room = self.rooms[room_index]
        self.rooms.remove(self.rooms[room_index])

    def draw_room(self):
        system("cls")
        room_fill = [""]

        # Bold
        print(formats.Bold  + self.current_room.name + formats.Reset)
        print(formats.Italic + self.current_room.description + formats.Reset_Italic)

        for y in range(0,self.current_room.size_y):
            for x in range(0,self.current_room.size_x):
                if x == self.player.x and y == self.player.y:
                    room_fill.append("😱")
                else:
                    room_fill.append("  ")

        i = 1
        accounted_for_double = False
        for y in range(0,self.current_room.size_y):
            if (y == 0):
                for x in range(0,self.current_room.size_x+2):
                    print("🧱", end="")
                print("")
            for x in range(0,self.current_room.size_x):
                if x == 0:
                    print("🧱", end="")
              
                print(room_fill[i], end="")
                if x == self.current_room.size_x-1:
                    print("🧱", end="")
                i += 1
                
          
            print("")
            tekst = ""
            if y ==self.current_room.size_y-1:
                for x in range(0,self.current_room.size_x+2):
                    tekst += "🧱"
                tekst += "\n"
            print(tekst, end="")
        input("Press Enter for å se valg. ")

    

    
    def draw_room_with_choices(self, choices):
        self.draw_room()
        choices.append("Se brettet")
        option, index = pick(choices, "Velg hva du vil gjøre", indicator='=>', default_index=0, )
        if (index == len(choices)-1):
            choices.pop()
            self.draw_room_with_choices(choices=choices)  

        # EXAMPLE 
        if (option == "Opp"):
            self.player.y = self.player.y - 1 if (self.player.y != 0) else self.current_room.size_y-1
            choices.pop()
            self.draw_room_with_choices(choices=choices)  

        if (option == "Ned"):
            self.player.y = self.player.y + 1 if (self.player.y != self.current_room.size_y-1) else 0
            choices.pop()
            self.draw_room_with_choices(choices=choices)  

        if (option == "Venstre"):
            self.player.x = self.player.x - 1 if (self.player.x != 0) else self.current_room.size_x-1
            choices.pop()
            self.draw_room_with_choices(choices=choices)  

        if (option == "Høyre"):
            self.player.x = self.player.x + 1 if (self.player.x != self.current_room.size_x-1) else 0
            choices.pop()
            self.draw_room_with_choices(choices=choices)  

class Room:
    def __init__(self, x,y):
        self.x=x
        self.y=y
        self.title ="Room 1"

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y


r1 = Room(x=10,y=5)
r2 = Room(x=5,y=5)
p = Player(x=1,y=1)
cave = Cave()
level = Level([cave],p)
level.pick_room()
level.draw_room_with_choices(["Opp","Ned","Venstre","Høyre"])