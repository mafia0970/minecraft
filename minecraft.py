from json import load
from pyexpat import model
from tkinter import Button, Scale
from xml.dom.minidom import Entity
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *
wion = Ursina()



diamond = load_texture('texure\diamond.png')
stone= load_texture('texure\stone.png')
grass= load_texture("texure\grass.png")
sky_texture = load_texture("texure\sky.png")
dirt_texture =load_texture("texure\dirt.png")
ice = load_texture("texure\ice.png")
wood= load_texture("texure\wood.png")
leaf = load_texture('texure\leaf.jpg')
current_texture = grass
def update():
    global current_texture
    if held_keys['1']: current_texture = stone
    if held_keys['2']:current_texture = ice
    if held_keys['3']: current_texture = diamond
    if held_keys['4']: current_texture = wood
    if held_keys['5']: current_texture = leaf








class Sky(Entity):
    def _init_(self):

        super().__init__(
            parent = scene,
            model = "circle",
            Scale = 150,
            texture = sky_texture,
            double_sided =True
        )




    


class Voxel(Button):
    def __init__(self,position = (0,0,0),texture = grass):
        super().__init__(
            parent = scene,
            model = 'cube',
            color = color.white,
            texture = texture,
            position = position,
            origin_y = 0.5,
            highlight_color = color.lime,
        )


    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel(position= self.position + mouse.normal,texture =current_texture)
            if key == "right mouse down":
                destroy(self)



    
for z in range(20):
    for x in range (20):
        voxel = Voxel((x,0,z))





player = FirstPersonController()

sky= Sky()


















wion.run()
