# !/usr/bin/env python .
# Created Tuesday, June 20, 2018 .
# Blender 2.79 onlinepanel.py
# 
# Last update :
import mouseclick
import renderview
import mouse
def ackPanelSinglePass():#
    mouseX, mouseY = mouse.vecMouse(mouse)
    LocX = mouseX
    for x in range(546, 667):#
        if x == LocX:#
            x = 1
            break
    LocY = mouseY
    for y in range(343, 363):#
        if y == LocY:#
            y = 1
            break
    if x + y == 2:#
        renderview.setSingle(1)
        mouseclick.online.setx(1)
def ackPanelMultiPass():#
    mouseX, mouseY = mouse.vecMouse(mouse)
    LocX = mouseX
    for x in range(596, 767):#
        if x == LocX:#
            x = 1
            break
    LocY = mouseY
    for y in range(388, 412):#
        if y == LocY:#
            y = 1
            break
    if x + y == 2:#
        mouseclick.online.setx(1)
        renderview.setMulti(1)        
