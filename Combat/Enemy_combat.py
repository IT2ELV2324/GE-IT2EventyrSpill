import math
from Classes.index import Player
from Enemy.index import Enemy
from Enemy.index import check_if_within_reach_enemy
def enemy_combat():
    if (check_if_within_reach_enemy == True):
        combat = True
    while combat:
        Player.hp -= Enemy.attack
        combat = False
    
