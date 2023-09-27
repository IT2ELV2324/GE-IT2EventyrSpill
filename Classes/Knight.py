from Classes.index import Player

class Knight(Player):
    def __init__(self, hp=70, attack=4, name="Knight",reach=2,speed=2):
      super().__init__(hp, attack,name,reach,speed)