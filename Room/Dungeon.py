import index as room
from ..Enemy   import Goblin, Sentinel, Warrior
from random import randint

enemies = [Goblin, Sentinel, Warrior]

class Dungeon(room.Room):
    def __init__(self, name="Dungeon",  description="Du befinner deg nå i en dungeon og ser en fiende foran deg", enemy= enemies[randint(1, len(enemies))](), sizex = 6, sizey = 5):
        super().__init__(name, description, enemy, sizex, sizey,)
