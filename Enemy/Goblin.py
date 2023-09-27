import index as i

class Goblin(i.Enemey):
    def __init__(self, hp = 20, name = "Goblin", attack = 8, speed = 8, reach = 1):
       super().__init__(hp, name, attack, speed, reach) 

