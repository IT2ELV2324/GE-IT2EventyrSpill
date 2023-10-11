import math
from Classes.index import Player
from Enemy.index import Enemy

while (abs(Enemy.xpos - Player.xpos) <= Enemy.reach):
    Player.hp = Player.hp - Enemy.attack
    print(f"{Enemy.name} slo deg og gjorde {Enemy.attack} dmg, du har {Player.hp} hp igjen." )
    if Player.hp <= 0:
        print(f"Du ble drept av {Player.name}")
        #kjør evt gameOver funskjon
        break
