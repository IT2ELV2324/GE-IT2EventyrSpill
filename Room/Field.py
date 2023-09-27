import Room_Class as room


class Field(room.Room):
    def __init__(self, name="Gresslette",  description="Du befinner deg nå på en gresslette og ser en fiende foran deg.", enemy= "", distance = 40):
        super().__init__(name, description, enemy, distance)
