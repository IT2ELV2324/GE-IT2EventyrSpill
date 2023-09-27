from pick import pick

class Level:
    def __init__(self, rooms, player):
        self.rooms = rooms
        self.player = player
    
    def pick_room(self):
        choices = []
        for room in self.rooms:
            choices.append(room.title)
        option, index = pick(choices, "Velg et rom", indicator='=>', default_index=0)
        self.set_scene(index)

    def set_scene(self, room_index):
        self.current_room = self.rooms[room_index]
        self.rooms.remove(self.rooms[room_index])

    def draw_room(self):
        room_fill = [""]
        for y in range(0,self.current_room.y):
            for x in range(0,self.current_room.x):
                if x == self.player.x and y == self.player.y:
                    room_fill.append("x")
                else:
                    room_fill.append("o")

        i = 1
        for y in range(0,self.current_room.y):
            for x in range(0,self.current_room.x):
                print(room_fill[i], end="")
                i += 1
            print("")
        
        
                
        print(
        """      
        """)

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
level = Level([r1,r2],p)
level.pick_room()
level.draw_room()