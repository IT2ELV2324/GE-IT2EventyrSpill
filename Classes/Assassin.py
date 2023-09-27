from Classes.index import Player

class Assassin(Player):
    def __init__(self, name="Assassin", hp=30, attack=8,reach="1",speed=8):
      super.__init__(hp, attack,name,reach,speed)
