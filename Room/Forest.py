import index as room
from ..Enemy   import Goblin, Sentinel, Warrior
from random import randint

enemies = [Goblin, Sentinel, Warrior]

class Forest(room.Room):
    def __init__(self, name="Skog",  description="Du befinner deg nå i en skog og ser en fiende foran deg", enemy= enemies[randint(1, len(enemies))],  sizex = 6, sizey = 6,):
        super().__init__(name, description, enemy, sizex, sizey,)
