import random

class Enemy:
    def __init__(self, hp = 40, name = "Goon", attack = 3, speed = 2, reach = 1, xpos = 0, ypos = 0, apperance="🤢"):
        self.hp = hp
        self.name = name
        self.attack = attack
        self.speed = speed
        self.reach = reach
        self.xpos = xpos
        self.ypos = ypos
        self.apperance = apperance

    def check_if_within_reach_of_player (self, xpos,ypos):
         dif = abs(self.xpos - xpos) + abs(self.ypos - ypos)
         self.dif_to_player = dif
         if dif <= self.reach:
            return True
         else:
            return False    
    def wants_to_flee(self):
        # Let's assume that if the enemy's health drops below 30%, 
        # it starts considering fleeing, with the probability increasing 
        # as the health decreases.
        if self.hp < 12:  # 30% of 40
            flee_chance = (1 - (self.hp / 40))  # Calculate the chance to flee based on current health
            return random.random() < flee_chance
        return False
    
    def wants_to_defend(self, player_attack_strength):
        # If the enemy's health is less than twice the player's attack strength, 
        # there's a higher chance the enemy might decide to defend.
        # This is just a heuristic and can be adjusted as needed.
        if self.hp < 2 * player_attack_strength:
            return random.random() < 0.5
        return False




