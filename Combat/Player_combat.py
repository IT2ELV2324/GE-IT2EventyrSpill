import math
from os import system
from Classes.index import Player
from Enemy.index import Enemy

while (abs(Player.xpos - Enemy.xpos) <= Player.reach):
    Enemy.hp = Enemy.hp - Player.attack
    print(f"Du slo {Enemy.name} og gjorde {Player.attack} dmg, du har {Enemy.hp} hp igjen." )
    if Enemy.hp <= 0:
        print(f"Du drepte{Enemy.name}")
        #kjør evt. en levelUp funskjon
        break
