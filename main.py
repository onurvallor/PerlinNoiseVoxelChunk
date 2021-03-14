from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import glm, random
from block import *
from texture_handler import *

app = Ursina()

grass_texture = load_texture('assets/grass.png')

def generateBlockPositions(width, height, depth):
    blockSize = 1
    noiseScale = 10
    amplitude = 20
    offset = random.randrange(0,1000000)
    data = []
    for x in range(width):
        for y in range(height):
            for z in range(depth):
                noise = glm.perlin(glm.vec3(x/noiseScale + offset, y/noiseScale + offset, z/noiseScale + offset)) * amplitude
                if noise >= 0.5:
                    data.append([x*blockSize, y*blockSize, z*blockSize])
    return data

perlin = generateBlockPositions(16,32,16)

# for z in range(8):
#     for x in range(8):
#         for y in range(1):
#             block = Block(position=(x,y,z), texture=grass_texture)

block_list=[]
terrain = Entity()

for a in perlin:
    block = Block(position=(a[0],a[1],a[2]), parent=terrain)
    block_list.append(block)

terrain.combine()
player = FirstPersonController(gravity=0)
player.add_script(NoclipMode())




def update():
    player.y += held_keys['q'] * 1
    player.y -= held_keys['e'] * 1
    
    # cast = boxcast(player.world_position, thickness=(10,10), debug=True)
    # print(cast.entities)
    # for block in block_list:
    #    if block not in cast.entities:
    #        block.visible = False
    #    elif block in cast.entities:
    #        block.visible = True

app.run()