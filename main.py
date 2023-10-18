from Classes.index import Player
from Classes.Assassin import Assassin
from Classes.Knight import Knight
from Classes.Mercenary import Mercenary
from Classes.Sharpshooter import Sharpshooter

from Room.Cave import Cave
from Room.Dungeon import Dungeon
from Room.Bridge import Bridge
from Room.Field import Field
from Room.Forest import Forest
import time
import random


from level import Level, pick_with_keyboard




p = Player(xpos
           =2,ypos=2, speed=2)


cave = Cave()
cave.enemy.xpos = 3
cave.enemy.ypos = 3
dungon = Dungeon()

bridge = Bridge()
field = Field()
field.enemy.xpos = 3
field.enemy.ypos = 3
forest = Forest(sizex=50,sizey=25)

level = Level([cave,dungon,bridge,field,forest],p)
level.print_story([
    'Du gikk en tur i skogen og kom over en hule.',
'Ut av hulen kom det en musikk fylt av sorg og håp.',
'Musikken trekker deg inn. Gjennom hulen kommer du til et mystisk sted.',
'Alt du klarer å tenke på er å slå den onde Slemsing.',
'En raspete dame stemme snakker til deg: "Hva er din historie?"'
])
def say_hi():
    print("hade!")


def movement():
    i = 0


    while i < level.player.speed:
        choices = []
        if (level.player.ypos != 0):
            choices.append("⬆️  Opp")
        if (level.player.ypos != level.current_room.size_y-1):
            choices.append("🔽 Ned")
        if (level.player.xpos != 0):
            choices.append("◀️  Venstre")
        if (level.player.xpos != level.current_room.size_x-1):
            choices.append("▶️  Høyre")
        choices.append("✖️  Avslutt")
        option, index = pick_with_keyboard(choices, "Hvilken vei vil du gå? ")
        

        if option == "⬆️  Opp":
            level.player.ypos = level.player.ypos - 1
        elif option == "🔽 Ned":
            level.player.ypos = level.player.ypos + 1
        elif option == "◀️  Venstre":
            level.player.xpos = level.player.xpos - 1
        elif option == "▶️  Høyre":
            level.player.xpos = level.player.xpos + 1
        elif option == "✖️  Avslutt":
            i = level.player.speed
        
        if (level.current_room.enemy.xpos == level.player.xpos and level.current_room.enemy.ypos == level.player.ypos):
            print("\033c", end="") 
            print(f"😮 Du ble angrepet av en {level.current_room.enemy.name}!")
            time.sleep(1)
            level.combat()
        
        else:
            # A random chance the enemy will attack the player if enemy.check_if_within_reach_of_player returns True. Higher chance the closer the player is to the enemy.
            if level.current_room.enemy.check_if_within_reach_of_player(level.player.xpos, level.player.ypos):
                dif = level.current_room.enemy.dif_to_player
                chance = 1 - (dif / level.current_room.enemy.reach)
                if random.random() < chance:
                    print("\033c", end="") 
                    print(f"😮 Du ble angrepet av en {level.current_room.enemy.name}!")
                    time.sleep(1)
                    level.combat()
            
        level.draw_room()
        i = i + 1

    level.draw_room_with_choices({
    "Velg nytt rom": new_room,
    "Beveg deg": movement,
})


def pick_class():
    classes = [Assassin(), Knight(), Mercenary(), Sharpshooter()]
    choices = []
    for klasse in classes:
        choices.append(klasse.name)
    option, index = pick_with_keyboard(choices, "Velg en klasse: ")
    level.player = classes[index]


def new_room():
    level.pick_room()
    level.draw_room_with_choices({
    "Velg nytt rom": new_room,
    "Beveg deg": movement,
})

pick_class()
new_room()