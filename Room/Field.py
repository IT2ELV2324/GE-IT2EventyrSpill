import index as room


class Field(room.Room):
    def __init__(self, name="Gresslette",  description="Du befinner deg nå på en gresslette og ser en fiende foran deg.", enemy= "", sizex = 10, sizey = 6,):
        super().__init__(name, description, enemy, sizex, sizey,)
