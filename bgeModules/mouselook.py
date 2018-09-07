# !/usr/bin/env python .
# Created Monday, August 20, 2018 .
# Blender 2.79 mouselook.py
# 
# Last update :

from bge import logic, render
from mathutils import Vector
class MouseLook:#

    def __init__(self, cont):#

        self.cont = cont

        self.sen_mouse = self.cont.sensors["mouse"]

        self.act_rotx = self.cont.actuators["rotx"]
        self.act_rotz = self.cont.actuators["rotz"]

        self.cont.activate(self.act_rotx)        
        self.cont.activate(self.act_rotz) 

        x = render.getWindowWidth()//2
        y = render.getWindowHeight()//2
        self.screen_center = (x, y)

        render.setMousePosition(*self.screen_center)

    def getMouseOffset(self):#

        vec_screencenter = Vector(self.screen_center)
        vec_mouseposition = Vector(self.sen_mouse.position)

        return vec_mouseposition - vec_screencenter


    def main(self):#

        vec_offset = self.getMouseOffset()
        vec_offset *= -0.005
        self.act_rotx.dRot = [vec_offset.y, 0, 0]
        self.act_rotz.dRot = [0, 0, vec_offset.x]
        render.setMousePosition(*self.screen_center)

mouse_look = MouseLook(logic.getCurrentController())
init = False  
def main():
    global init
    if init:#   
        mouse_look.main()
    else:#
        init = True
    
