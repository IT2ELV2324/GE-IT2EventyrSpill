class Enemy:
    def __init__(self, hp = 40, name = "Goon", attack = 3, speed = 2, reach = 1, xpos = 0, ypos = 0, apperance="🤢"):
        self.hp = hp
        self.name = name
        self.attack = attack
        self.speed = speed
        self.reach = reach
        self.xpos = xpos
        self.ypos = ypos
        self.apperance = apperance


def check_if_within_reach_enemy(self, xpos,ypos):
      if (abs(self.xpos - Enemy.xpos) <= self.reach) and abs(self.ypos - Enemy.ypos) <= self.reach:
         return True
      else:
         return False




