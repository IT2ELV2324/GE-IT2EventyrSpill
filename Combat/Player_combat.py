import math
from os import system
from Classes.index import Player
from Enemy.index import Enemy
from Classes.index import check_if_within_reach_player

def player_combat():
    if (check_if_within_reach_player == True):
        combat = True
    while combat:
        Enemy.hp -= Player.attack



