

class Room():
    def __init__(self, name,  description, enemy, sizex, sizey, exit="Etter å ha drept fienden din ser du en dør bak dem og går gjennom den."):

        self.name = name
        self.description = description
        self.enemy = enemy
        self.size_x = sizex
        self.size_y = sizey
        self.exit = exit


    def describe(self):
        print(self.description)
        print(f"Dette er en {self.enemy}.")
        print("Du gjør deg klar for kamp.")


class Boss_Room(Room):
    def __init__(self, name, description= "Du befinner deg nå i et rom med en diger trone og ser en fiende foran deg", enemy="Slemsing", sizex= 8, sizey = 8):
        super().__init__(name, description, enemy, sizex, sizey)


