from Enemy.index import Enemy

class Goblin(Enemy):
    def __init__(self, hp = 20, name = "Goblin", attack = 8, speed = 8, reach = 1, xpos = 0, ypos = 0, apperance = "👹"):
       super().__init__(hp, name, attack, speed, reach, xpos, ypos) 

