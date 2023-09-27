import Room_Class as room


class Forest(room.Room):
    def __init__(self, name="Skog",  description="Du befinner deg nå i en skog og ser en fiende foran deg", enemy= "", distance = 25):
        super().__init__(name, description, enemy, distance)
