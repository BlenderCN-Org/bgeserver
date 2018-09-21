# !/usr/bin/env python .
# Created Wednesday, June 20, 2018 .
# Blender 2.79 mouse.py
# 
# Last update :
from bge import logic
import serverconnect
class MouseUser:#_____________________________________________________________________________:(
    def __init__(self):#
        self.user = 0
    def count(self):#
        self.user  = togMouse.get_n() + 1
        togMouse.set_n(self.user)
    def decount(self):#
        out = togMouse.get_n() - 1
        togMouse.set_n(out)
mouseUser = MouseUser()
def TogMouse():#
    n = 0
    def func():#
        print('> TogMouse', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_
togMouse = TogMouse()
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

