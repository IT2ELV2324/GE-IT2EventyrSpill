from Room.index import Room
from Enemy.Bombardier import Bombardier
from Enemy.Sentinel import Sentinel
from random import randint

enemies = [Bombardier, Sentinel]

class Field(Room):
    def __init__(self, name="Gresslette",  description="Du befinner deg nå på en gresslette og ser en fiende foran deg.",  enemy= enemies[randint(0, len(enemies)-1)](), sizex = 10, sizey = 6,):
        super().__init__(name, description, enemy, sizex, sizey,material="🌾")
