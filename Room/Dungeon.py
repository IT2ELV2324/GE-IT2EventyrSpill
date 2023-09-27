import index as room


class Dungeon(room.Room):
    def __init__(self, name="Dungeon",  description="Du befinner deg nå i en dungeon og ser en fiende foran deg", enemy= "", sizex = 6, sizey = 5):
        super().__init__(name, description, enemy, sizex, sizey,)
