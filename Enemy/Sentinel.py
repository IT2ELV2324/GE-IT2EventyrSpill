import index as i

class Sentinel(i.Enemey):
    def __init__(self, hp = 70, name = "Sentinel", attack = 4, speed = 2, reach = 1, xpos = 50, ypos = 0):
       super().__init__(hp, name, attack, speed, reach, xpos, ypos) 
