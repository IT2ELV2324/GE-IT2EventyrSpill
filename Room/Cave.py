import index as room


class Cave(room.Room):
    def __init__(self, name="Hule",  description="Du befinner deg nå i en hule og ser en fiende foran deg", enemy= "", sizex = 5, sizey = 4,):
        super().__init__(name, description, enemy, sizex, sizey,)
