import math
from Classes.index import Player
from Enemy.index import Enemy

def combat_loop():

    if (abs(Player.xpos - Enemy.xpos) <= Player.reach 
        and abs(Player.ypos - Enemy.ypos) <= Player.reach
        and abs(Enemy.xpos - Enemy.xpos) <= Enemy.reach
        and abs(Enemy.ypos - Player.ypos) <= Enemy.reach):
        combat = True

    while combat:
        if Player.speed > Enemy.speed:  
            Enemy.hp = Enemy.hp - Player.attack
            print(f"Du slo {Enemy.name} og gjorde {Player.attack} dmg, {Enemy.name} har {Enemy.hp} hp igjen." )
        else:
            Player.hp = Player.hp - Enemy.attack
            print(f"{Enemy.name} slo deg og gjorde {Enemy.attack} dmg, du har {Player.hp} hp igjen." )
        if Player.hp == 0 or Enemy.hp == 0:
            if Player.hp <= 0:
                print(f"Du ble drept av",Enemy.name)
                #kjør evt GameOver funskjon?
            if Enemy.hp <= 0:
                print(f"Du drepte", Enemy.name)
            #kjør feks. en funskjon som øker nivået og gjør Player sterkere her
            break
        