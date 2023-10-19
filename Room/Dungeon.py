from Room.index import Room
from Enemy.Goblin import Goblin
from Enemy.Sentinel import Sentinel
from Enemy.Warrior import Warrior
from random import randint

enemies = [Goblin, Sentinel, Warrior]

class Dungeon(Room):
    def __init__(self, name="Dungeon",  description="Du befinner deg nå i en dungeon og ser en fiende foran deg",  enemy= enemies[randint(0, len(enemies)-1)](), sizex = 6, sizey = 5):
        super().__init__(name, description, enemy, sizex, sizey,material="⛓️")
