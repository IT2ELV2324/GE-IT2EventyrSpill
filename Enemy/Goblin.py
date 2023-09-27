from Enemy.index import Enemy

class Goblin(Enemy):
    def __init__(self, hp = 20, name = "Goblin", attack = 8, speed = 8, reach = 1, xpos = 50, ypos = 0):
       super().__init__(hp, name, attack, speed, reach, xpos, ypos) 

