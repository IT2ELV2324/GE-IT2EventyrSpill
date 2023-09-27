import index as room


class Forest(room.Room):
    def __init__(self, name="Skog",  description="Du befinner deg nå i en skog og ser en fiende foran deg", enemy= "", sizex = 6, sizey = 6,):
        super().__init__(name, description, enemy, sizex, sizey,)
