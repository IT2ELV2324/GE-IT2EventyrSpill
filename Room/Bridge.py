import index as room
from ..Enemy   import Bombardier, Sentinel
from random import randint

enemies = [Bombardier, Sentinel]

class Bridge(room.Room):
    def __init__(self, name="Bro",  description="Du befinner deg nå på en bro og ser en fiende foran deg", enemy= enemies[randint(1, len(enemies))](), sizex= 11, sizey = 5):
        super().__init__(name, description, enemy, sizex, sizey,)
