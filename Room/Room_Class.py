

class Room():
    def __init__(self, name,  description, enemy, distance, size = 60, exit="Etter å ha drept fienden din ser du en dør bak dem og går gjennom den."):

        self.name = name
        self.description = description
        self.enemy = enemy
        self.distance = distance
        self.size = size
        self.exit = exit


    def print_distance(self):
        print(f"Det er {str(self.distance)}m avstand mellom deg og {self.enemy}.")

    def describe(self):
        print(self.description)
        print(f"Dette er en {self.enemy}.")
        self.print_distance()
        print("Du gjør deg klar for kamp.")


class Boss_Room(Room):
    def __init__(self, name, description= "Du befinner deg nå i et rom med en diger trone og ser en fiende foran deg", enemy="Slemsing", distance = "60m"):
        super().__init__(name, description, enemy, distance)


