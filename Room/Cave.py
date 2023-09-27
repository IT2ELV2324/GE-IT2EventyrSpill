from Room.index import Room
from Enemy.Goblin import Goblin
from Enemy.Warrior import Warrior
from random import randint

enemies = [Goblin, Warrior]

class Cave(Room):
    def __init__(self, name="Hule",  description="Du befinner deg nå i en hule og ser en fiende foran deg", enemy= enemies[randint(0, len(enemies)-1)](), sizex = 5, sizey = 4,):
        super().__init__(name, description, enemy, sizex, sizey, material="🪨 ")
