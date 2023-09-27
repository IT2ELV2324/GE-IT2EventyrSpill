class Enemy:
    def __init__(self, hp, name, attack, speed, reach):
        self.hp = hp
        self.name = name
        self.attack = attack
        self.speed = speed
        self.reach = reach


class Boss(Enemy):
    def __init__(self, hp, name, attack, speed, reach):
        super().__init__(hp, name, attack, speed, reach)




