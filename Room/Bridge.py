from Room.index import Room
from Enemy.Bombardier import Bombardier
from Enemy.Sentinel import Sentinel
from random import randint

enemies = [Bombardier, Sentinel]

class Bridge(Room):
    def __init__(self, name="Bro",  description="Du befinner deg nå på en bro og ser en fiende foran deg",  enemy= enemies[randint(0, len(enemies)-1)](), sizex= 11, sizey = 5):
        super().__init__(name, description, enemy, sizex, sizey,empty_material="🟫")
