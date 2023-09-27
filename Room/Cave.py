import index as room
from ..Enemy   import Goblin, Warrior
from random import randint

enemies = [Goblin, Warrior]

class Cave(room.Room):
    def __init__(self, name="Hule",  description="Du befinner deg nå i en hule og ser en fiende foran deg", enemy= enemies[randint(1, len(enemies))](), sizex = 5, sizey = 4,):
        super().__init__(name, description, enemy, sizex, sizey,)
