from Enemy.index import Enemy

class Bombardier(Enemy):
    def __init__(self, hp = 20, name = "Bombardier", attack = 5, speed = 3, reach = 10, xpos = 50, ypos = 0):
       super().__init__(hp, name, attack, speed, reach, xpos, ypos) 

