import Room_Class as room


class Bridge(room.Room):
    def __init__(self, name="Bro",  description="Du befinner deg nå på en bro og ser en fiende foran deg", enemy= "", distance = 40):
        super().__init__(name, description, enemy, distance)
