from ursina import *
from texture_handler import GrabBlockTexture

class Block(Button):

    def __init__(self, parent=None, position=(0,0,0), texture='white_cube'):
        verts = ((0,0,0), (1,0,0), (1, 1, 0), (0,1,0), (0,1,1), (1,1,1), (1,0,1), (0,0,1))
        tris = (0, 2, 1, 0, 3, 2, 2,3,4,2,4,5,1,2,5,1,5,6,0,7,4,0,4,3,5,4,7,5,7,6,0,6,7,0,1,6)
        uvs = ((1.0, 0.0), (0.0, 1.0), (0.0, 0.0), (1.0, 1.0))
        norms = ((0,0,-1),) * len(verts)
        colors = (color.black,color.black,color.black,color.black)
        super().__init__(parent=scene, position=position, model=Mesh(vertices=verts, triangles=tris, uvs=uvs, normals=norms, colors=colors), origin_y=0.5, color=color.white, highlight_color=color.color(0,0,0.7))
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                block = Block(position=self.position + mouse.normal, texture="white_cube")
            if key == 'right mouse down':
                print("This is position: ", self.position)
                destroy(self)
            if key == 'x':
                application.quit()

class BlockType():
    def __init__(self):
        self.block_type = 1
    def switch_block(self):
        return self.block_type