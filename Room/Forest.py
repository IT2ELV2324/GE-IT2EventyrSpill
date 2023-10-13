from Room.index import Room
from Enemy.Goblin import Goblin
from Enemy.Sentinel import Sentinel
from Enemy.Warrior import Warrior
from random import randint

enemies = [Goblin, Sentinel, Warrior]


class Forest(Room):
    def __init__(self, name="Skog",  description="Du befinner deg nå i en skog og ser en fiende foran deg",  enemy= enemies[randint(0, len(enemies)-1)](),  sizex = 6, sizey = 6,):
        super().__init__(name, description, enemy, sizex, sizey,material="🌲", empty_material="🟩")
