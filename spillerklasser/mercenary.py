import index as idx

class Mercenary(idx.Player):
    def __init__(self, hp=40, attack=5, name="Mercenary",reach=4,speed=4):
      super.__init__(hp, attack,name,reach,speed)