import index as room
from ..Enemy   import Bombardier, Sentinel
from random import randint

enemies = [Bombardier, Sentinel]
class Field(room.Room):
    def __init__(self, name="Gresslette",  description="Du befinner deg nå på en gresslette og ser en fiende foran deg.", enemy= enemies[randint(1, len(enemies))](), sizex = 10, sizey = 6,):
        super().__init__(name, description, enemy, sizex, sizey,)
