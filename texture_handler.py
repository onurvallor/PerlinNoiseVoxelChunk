from ursina import *

class GrabBlockTexture():
    def __init__(self):
        self.grass_texture = load_texture('assets/grass.png')
    def run_ursina(self):
        app = Ursina()