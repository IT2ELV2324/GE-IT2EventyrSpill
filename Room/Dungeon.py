import Room_Class as room


class Dungeon(room.Room):
    def __init__(self, name="Dungeon",  description="Du befinner deg nå i en dungeon og ser en fiende foran deg", enemy= "", distance = 25):
        super().__init__(name, description, enemy, distance)
