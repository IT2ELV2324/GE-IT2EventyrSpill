import index as i

class Boss(i.Enemy):
    def __init__(self, hp = 100, name = "Slemsing", attack = 9, speed = 3, reach = 5, xpos = 50, ypos = 0):
        super().__init__(hp, name, attack, speed, reach, xpos, ypos)
