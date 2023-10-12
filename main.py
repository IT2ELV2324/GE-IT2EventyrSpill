from Classes.index import Player
from Classes.Assassin import Assassin

from Room.Cave import Cave
from Room.Dungeon import Dungeon
from Room.Bridge import Bridge
from Room.Field import Field
from Room.Forest import Forest

from level import Level



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

def become_assasin():
    level.player = Assassin()
    new_room()

def new_room():
    level.pick_room()
    level.draw_room_with_choices({
    "Si hade": say_hi,
    "Bli Assasin": become_assasin,
    "Velg nytt rom": new_room
})

new_room()