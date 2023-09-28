from Classes.index import Player

class Sharpshooter(Player):
    def __init__(self, name="Sharpshooter", hp=20, attack=5, reach=10,speed=3):
      super().__init__(hp, attack,name,reach,speed)