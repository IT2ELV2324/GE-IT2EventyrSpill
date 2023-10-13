from Classes.index import Player
from Classes.Assassin import Assassin

from Room.Cave import Cave
from Room.Dungeon import Dungeon
from Room.Bridge import Bridge
from Room.Field import Field
from Room.Forest import Forest

from level import Level, pick_with_keyboard




p = Player(xpos=2,ypos=2, speed=2)

cave = Cave()
dungon = Dungeon()
bridge = Bridge()
field = Field()
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
            choices.append("Opp")
        if (level.player.ypos != level.current_room.size_y-1):
            choices.append("Ned")
        if (level.player.xpos != 0):
            choices.append("Venstre")
        if (level.player.xpos != level.current_room.size_x-1):
            choices.append("Høyre")
        option, index = pick_with_keyboard(choices)

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

    level.draw_room_with_choices({
    "Si hade": say_hi,
    "Bli Assasin": become_assasin,
    "Velg nytt rom": new_room,
    "Beveg deg": movement,
})
    



def become_assasin():
    level.player = Assassin()
    new_room()

def new_room():
    level.pick_room()
    level.draw_room_with_choices({
    "Si hade": say_hi,
    "Bli Assasin": become_assasin,
    "Velg nytt rom": new_room,
    "Beveg deg": movement,
})

new_room()