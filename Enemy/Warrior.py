from Enemy.index import Enemy

class Warrior(Enemy):
    def __init__(self, hp = 40, name = "Warrior", attack = 5, speed = 4, reach = 4, xpos = 50, ypos = 0):
       super().__init__(hp, name, attack, speed, reach, xpos, ypos) 
