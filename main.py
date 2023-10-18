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


def player_combat():
    if (level.player.check_if_within_reach_player(level.current_room.enemy.xpos, level.current_room.enemy.ypos)):
        combat = True
    while combat:
        level.current_room.enemy.hp -= level.player.attack

def enemy_combat():
    if (level.current_room.enemy.check_if_within_reach_enemy(level.player.xpos, level.player.ypos)):
        combat = True
    while combat:
        level.player.hp -= level.current_room.enemy.attack
        combat = False

def combat_loop():
    combat = True
    if (abs(level.player.xpos - level.current_room.enemy.xpos) <= level.player.reach 
        and abs(level.player.ypos - level.current_room.enemy.ypos) <= level.player.reach
        and abs(level.current_room.enemy.xpos - level.current_room.enemy.xpos) <= level.player.enemy.reach
        and abs(level.current_room.enemy.ypos - level.player.ypos) <= level.current_room.enemy.reach):
        combat = True

    while combat:
        print("damn")
        if level.player.speed > level.current_room.enemy.speed:  
            level.current_room.enemy.hp = level.current_room.enemy.hp - level.player.attack
            level.player.hp -= level.current_room.enemy.attack
            print(f"Du slo {level.current_room.enemy.name} og gjorde {level.player.attack} dmg, {level.current_room.enemy.name} har {level.current_room.enemy.hp} hp igjen." )
            combat = False
        else:
            level.player.hp = level.player.hp - level.current_room.enemy.attack
            level.current_room.enemy.hp -= level.player.attack
            print(f"{level.current_room.enemy.name} slo deg og gjorde {level.current_room.enemy.attack} dmg, du har {level.player.hp} hp igjen." )
            combat = False

def movement():
    i = 0


    while i < level.player.speed:
        choices = []
        if (level.player.ypos != 0):
            choices.append("Opp")
        if (level.player.ypos != level.current_room.size_y-1):
            choices.append("Ned")
        if (level.player.xpos != 0):
            choices.append("Venstre")
        if (level.player.xpos != level.current_room.size_x-1):
            choices.append("Høyre")
        option, index = pick_with_keyboard(choices, "Hvilken vei vil du gå? ")

        if option == "Opp":
            level.player.ypos = level.player.ypos - 1
        elif option == "Ned":
            level.player.ypos = level.player.ypos + 1
        elif option == "Venstre":
            level.player.xpos = level.player.xpos - 1
        elif option == "Høyre":
            level.player.xpos = level.player.xpos + 1
        level.draw_room()
        i = i + 1
    if (level.player.check_if_within_reach_player(level.current_room.enemy.xpos, level.current_room.enemy.ypos)):
        level.draw_room_with_choices({
        "Si hade": say_hi,
        "Bli Assasin": become_assasin,
        "Velg nytt rom": new_room,
        "Beveg deg": movement,
        "Angrep": player_combat
    })
    elif (level.player.check_if_within_reach_player(level.current_room.enemy.xpos, level.current_room.enemy.ypos) and level.current_room.enemy.check_if_within_reach_enemy(level.player.xpos, level.player.ypos)):
        level.draw_room_with_choices({
        "Si hade": say_hi,
        "Bli Assasin": become_assasin,
        "Velg nytt rom": new_room,
        "Beveg deg": movement,
        "Angrep": combat_loop
    })
    else: 
        level.draw_room_with_choices({
        "Si hade": say_hi,
        "Bli Assasin": become_assasin,
        "Velg nytt rom": new_room,
        "Beveg deg": movement,
    })

def become_assasin():
    level.player = Assassin()
    new_room()

def pick_class():
    classes = [Assassin(), Knight(), Mercenary(), Sharpshooter()]
    choices = []
    for klasse in classes:
        choices.append(klasse.name)
    option, index = pick_with_keyboard(choices, "Velg en klasse: ")
    level.player = classes[index]
def stat():
    level.pick_stat()
    new_room()

def new_room():
    level.pick_room()
    level.draw_room_with_choices({
    "Si hade": say_hi,
    "Bli Assasin": become_assasin,
    "Velg nytt rom": new_room,
    "Beveg deg": movement,
    "ny stat": stat,
})

pick_class()
new_room()