# !/usr/bin/env python .
# Created Wednesday, June 20, 2018 .
# Blender 2.79 mouse.py
# 
# Last update :
from bge import logic
import serverconnect
def MouseX():#
    n = 0
    def func():#
        print('> MouseX ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
mouseX = MouseX()

def MouseY():#
    n = 0
    def func():#
        print('> MouseY ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
mouseY = MouseY()#

def mouseLeftClick():#
    cont = logic.getCurrentController()
    own = cont.owner
    sens = cont.sensors['LeftClick']
    if sens.positive:#
        serverconnect.Disconnect(1)
        mousePosition = sens.position
        mouseX.set_n(mousePosition[0])
        mouseY.set_n(mousePosition[1])
def vecMouse(mouse):#
    return mouseX.get_n(), mouseY.get_n()
############################

