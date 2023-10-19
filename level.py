import keyboard

from os import system
import random
import math
import time

class formats:
    Bold = "\x1b[1m"
    Dim = "\x1b[2m"
    Italic = "\x1b[3m"
    Underlined = "\x1b[4m"
    Blink = "\x1b[5m"
    Reverse = "\x1b[7m"
    Hidden = "\x1b[8m"
    # Reset part
    Reset = "\x1b[0m"
    Reset_Bold = "\x1b[21m"
    Reset_Dim = "\x1b[22m"
    Reset_Italic = "\x1b[23m"
    Reset_Underlined = "\x1b[24"
    Reset_Blink = "\x1b[25m"
    Reset_Reverse = "\x1b[27m"
    Reset_Hidden = "\x1b[28m"

def pick_with_keyboard(options, context):
    time.sleep(0.2)
    current_index = 0

    # Display the initial menu
    def display_menu(index):
        print("\033c", end="")  # Clear the console
        print(context)
        print()
        for idx, option in enumerate(options):
            if idx == index:
                print(f"=> {option}")  # Indicate the current selection with an arrow
            else:
                print(f"   {option}")

    display_menu(current_index)


    while True:
        if keyboard.is_pressed('down'):
            current_index = (current_index + 1) % len(options)
            display_menu(current_index)
            time.sleep(0.2)  # Prevents rapid cycling

        elif keyboard.is_pressed('up'):
            current_index = (current_index - 1) % len(options)
            display_menu(current_index)
            time.sleep(0.2)

        elif keyboard.is_pressed('enter'):
            break

    return options[current_index], current_index

class Level:
    def __init__(self, rooms, player, defx=0, defy=0):
        self.rooms = rooms
        self.player = player
        self.defy = player.ypos
        self.defx = player.xpos

    def pick_room(self):
        choices = []
        self.player.xpos, self.player.ypos = self.defx, self.defy
        for room in self.rooms:
            choices.append(room.name)
        if (len(choices) <= 0):
            print("\033c", end="")  # Clear the console
            print(" 🥳 Du har vunnet spillet! ")
            time.sleep(2)
            exit()
            return
        option, index = pick_with_keyboard(choices, "Velg et rom å gå inn i: ")
        self.set_scene(index)

    def is_enemy_within_reach(self):
        return self.player.check_if_within_reach_player(self.current_room.enemy.xpos, self.current_room.enemy.ypos)

    def combat(self):
        player_defending = False  # Track if the player is currently defending
        enemy_defending = False  # Track if the enemy is currently defending

        while self.player.hp > 0 and self.current_room.enemy.hp > 0:
            # Display combat menu
            option, index = pick_with_keyboard(["⚔️  Angrip", "🛡️  Forsvar", "🏃 Løp"], "Velg en handling:")
            print("\033c", end="")  # Clear the console

            # Player's turn
            if option == "⚔️  Angrip":
                print(f"⚔️  {self.player.name} angriper!")
                self.current_room.enemy.hp -= self.player.attack
                if self.current_room.enemy.hp <= 0:
                    print(f"☠️  {self.current_room.enemy.name} er død!")
                    time.sleep(3)
                    self.pick_stat()
                    self.rooms.remove(self.current_room)  # Remove the room
                    self.pick_room()
                    self.draw_room_with_choices(self.ads_cache)
                    return

            elif option == "🛡️  Forsvar":
                if random.random() <= 0.75:  # 75% chance
                    heal_amount = 1.5  # Assuming a fixed heal value, adjust as needed
                    self.player.hp += heal_amount
                    print(f"🛡️  {self.player.name} forsvarte og helbredet seg selv for {heal_amount} poeng!")
                else:
                    player_defending = True
                    print(f"🛡️  {self.player.name} forbereder seg på å forsvare!")

            elif option == "🏃 Løp":
                print(f"🏃 {self.player.name} løper vekk!")
                time.sleep(1)
                self.pick_room()
                self.draw_room_with_choices(self.ads_cache)
                return

            # Enemy's turn
            if self.current_room.enemy.wants_to_defend(self.player.attack):
                if random.random() <= 0.75:  # 75% chance
                    heal_amount = 1.5  # Assuming a fixed heal value for the enemy, adjust as needed
                    self.current_room.enemy.hp += heal_amount
                    print(f"🛡️  {self.current_room.enemy.name} forsvarte og helbredet seg selv for {heal_amount} poeng!")
                else:
                    enemy_defending = True
                    print(f"🛡️  {self.current_room.enemy.name} forbereder seg på å forsvare!")
                time.sleep(2)
            elif self.current_room.enemy.wants_to_flee():
                print(f"😨 {self.current_room.enemy.name} ser redd ut og prøver å løpe vekk!")
                time.sleep(3)
                # Calculate potential new positions
                potential_positions = {
                    "up": (self.current_room.enemy.xpos, max(0, self.current_room.enemy.ypos - self.current_room.enemy.speed)),
                    "down": (self.current_room.enemy.xpos, min(self.current_room.size_y-1, self.current_room.enemy.ypos + self.current_room.enemy.speed)),
                    "left": (max(0, self.current_room.enemy.xpos - self.current_room.enemy.speed), self.current_room.enemy.ypos),
                    "right": (min(self.current_room.size_x-1, self.current_room.enemy.xpos + self.current_room.enemy.speed), self.current_room.enemy.ypos)
                }

                # Calculate the distances to the player for each potential position
                distances = {
                    direction: ((self.player.xpos - x)**2 + (self.player.ypos - y)**2)**0.5
                    for direction, (x, y) in potential_positions.items()
                }

                # Determine the direction with the maximum distance from the player
                flee_direction = max(distances, key=distances.get)

                # Update the enemy's position
                self.current_room.enemy.xpos, self.current_room.enemy.ypos = potential_positions[flee_direction]
                
                # Close the combat menu and let the player move
                self.draw_room_with_choices(self.ads_cache)
                return
            else:
                print(f"⚔️  {self.current_room.enemy.name} angriper!")
                if player_defending:  # If player chose to defend
                    damage_taken = self.current_room.enemy.attack / 2  # Half damage
                    self.player.hp -= damage_taken
                    print(f"🛡️  {self.player.name} tok bare {damage_taken} skade på grunn av forsvar!")
                    player_defending = False  # Reset the defending flag
                    time.sleep(2)
                else:
                    self.player.hp -= self.current_room.enemy.attack
                    if enemy_defending:
                        damage_taken = self.player.attack / 2  # Half damage
                        self.current_room.enemy.hp -= damage_taken
                        print(f"🛡️  {self.current_room.enemy.name} tok bare {damage_taken} skade på grunn av forsvar!")
                        enemy_defending = False  # Reset the defending flag
                        time.sleep(2)
                    else:
                        self.current_room.enemy.hp -= self.player.attack
                        time.sleep(1)
            
            time.sleep(1)
            if self.player.hp <= 0:
                print("\033c", end="")  # Clear the console
                print(f"☠️  {self.player.name} er død!")
                print("😭 Du har tapt spillet! ")
                time.sleep(2)
                return
            elif self.current_room.enemy.hp <= 0:
                print(f"☠️  {self.current_room.enemy.name} er død!")
                time.sleep(3)
                self.pick_stat()
                self.rooms.remove(self.current_room)  # Remove the room
                self.pick_room()
                self.draw_room_with_choices(self.ads_cache)
                return
            else: 
                self.display_stats()



    def pick_stat(self):
        print("\033c", end="")  # Clear the console
        def f(x):
            L =5
            k = 0.05
            x0 = 10
            return L / (1 + math.e**(k*(x-x0)))
 
        option, index = pick_with_keyboard([f"❤️  HP ({self.player.hp})", f"⚔️  Skade ({self.player.attack})", f"📏 Rekkevidde ({self.player.reach})", f'👟 Fart {self.player.speed}'], "📈 Velg en stat å oppgradere: ")

        stat_list = list(self.player.__dict__.keys())
        current_value = getattr(self.player, stat_list[index])
        new_value =   round(current_value*
        f(current_value))
        setattr(self.player, stat_list[index], new_value)

        new_value = current_value if new_value <= current_value else new_value

        if (new_value == current_value):
            print(f"❗  Du har nådd maks for {option}")
            time.sleep(2)
            self.pick_stat()
        else:
            print(f"\n🎉 {option.replace(str(current_value), str(new_value))} har blitt oppgradert!")
            time.sleep(1)


    def set_scene(self, room_index):
        self.current_room = self.rooms[room_index]

    def draw_room(self):
        system("cls")
        room_fill = [""]

        # Bold
        print(formats.Bold + self.current_room.name + formats.Reset)
        print(formats.Italic + self.current_room.description + formats.Reset_Italic)

        for y in range(0, self.current_room.size_y):
            for x in range(0, self.current_room.size_x):
                if x == self.player.xpos and y == self.player.ypos:
                    room_fill.append(self.player.apperance)
                elif x == self.current_room.enemy.xpos and y == self.current_room.enemy.ypos:
                    room_fill.append(self.current_room.enemy.apperance)
                else:
                    room_fill.append(self.current_room.empty_material)
                

        i = 1
        for y in range(0, self.current_room.size_y):
            if (y == 0):
                for x in range(0, self.current_room.size_x+2):
                    print(self.current_room.material, end="")
                print("")
            for x in range(0, self.current_room.size_x):
                if x == 0:
                    print(self.current_room.material, end="")

                print(room_fill[i], end="")
                if x == self.current_room.size_x-1:
                    print(self.current_room.material, end="")
                i += 1

            print("")
            tekst = ""
            if y == self.current_room.size_y-1:
                for x in range(0, self.current_room.size_x+2):
                    tekst += self.current_room.material
                tekst += "\n"
            print(tekst, end="")
        print("")
        print("Trykk på enter for å fortsette")
        keyboard.wait("enter")

    def print_story(self, story):
        # Press enter to skip the story
        isSkipping = False
        def skip_story():
            nonlocal isSkipping
            isSkipping = True
        keyboard.add_hotkey('enter', skip_story)
            
        for line in story:
            for char in line:
                if (isSkipping):
                    break
                print(char, end='', flush=True)
                time.sleep(0.05)
            print()  # New line after each story line
            if (isSkipping):
                break
            time.sleep(1)  # Wait a second before the next line
    def display_stats(self):
        system("cls")

        stats = list(self.player.__dict__.values())

        print("📊 Sånn ser statsene ut nå:")
        print()
        print(f"❤️  Din HP: {str(stats[0])}")
        print(f"❤️  {self.current_room.enemy.name} HP: {self.current_room.enemy.hp}")
        print(f"⚔️  Din Skade: {str(stats[1])}")
        print(f"📏 Din Rekkevidde: {str(stats[2])}")
        print(f"👟 Din Fart: {str(stats[3])}")
        print()
        print()
        print("🔜 Trykk på enter for å fortsette")

        

        keyboard.wait("enter")

    def draw_room_with_choices(self, additional_choices):
        self.draw_room()
        self.ads_cache = additional_choices

        if self.is_enemy_within_reach():
            additional_choices["Angrip"] = self.combat
        
        option, index = pick_with_keyboard([*additional_choices.keys(), "Se stats", "Se brettet"], "Hva vil du gjøre?")

        if (option in additional_choices.keys()):
            additional_choices[option]()

        if (option == "Se stats"):
            self.display_stats()
            self.draw_room_with_choices(additional_choices)

            

        if (option == "Se brettet"):
            self.draw_room_with_choices(additional_choices)

        if (option == "Opp"):
            self.player.ypos = max(
                0, self.player.ypos - self.player.speed)

            self.draw_room_with_choices(additional_choices)

        if (option == "Ned"):
            self.player.ypos = min(self.current_room.size_y-1, self.player.ypos + self.player.speed)
            self.draw_room_with_choices(additional_choices)

        if (option == "Venstre"):
            self.player.xpos =max(0, self.player.xpos - self.player.speed)

            self.draw_room_with_choices(additional_choices)

        if (option == "Høyre"):
            self.player.xpos = min(
                self.current_room.size_x-1, self.player.xpos + self.player.speed)
            

            self.draw_room_with_choices(additional_choices)

