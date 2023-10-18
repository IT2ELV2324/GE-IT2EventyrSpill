import math
from Enemy.index import Enemy
class Player:
   def __init__(self, hp=0, attack=0, name="",reach=0,speed=0,xpos=10,ypos=0, apperance="👨"):
      self.hp = hp
      self.attack = attack
      self.reach = reach
      self.speed = speed
      self.name = name
      self.xpos = xpos
      self.ypos = ypos
      self.apperance = apperance
   


def check_if_within_reach_player(self, xpos,ypos):
      if (abs(self.xpos - Enemy.xpos) <= self.reach) and abs(self.ypos - Enemy.ypos) <= self.reach:
         return True
      else:
         return False

