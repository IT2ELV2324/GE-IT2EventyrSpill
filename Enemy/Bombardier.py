import index as i

class Bombardier(i.Enemey):
    def __init__(self, hp = 20, name = "Bombardier", attack = 5, speed = 3, reach = 10):
       super().__init__(hp, name, attack, speed, reach) 

