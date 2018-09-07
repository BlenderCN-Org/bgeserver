# !/usr/bin/env python .
# Created Sunday, August 26, 2018 .
# Blender 2.79 ackpanel.py
# 
# Last update 
#
###########################################
class Main:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Main' property.")
main = Main()
##########################
def ackPanelMain():#________________________Panel Loader 1._________________________________________________________:(
    LocX = mouseLocX.get_n() + viewPortX.get_n()
    for x in range(minLocX.get_n(), maxLocX.get_n()):#
        if x == LocX:#
            x = 1
            break
    LocY = mouseLocY.get_n() + viewPortY.get_n()
    for y in range(minLocY.get_n(), maxLocY.get_n()):#
        if y == LocY:#
            y = 1
            break
    if x + y == 2:#
        mainLoader.set_n(setMouse.get_n())
#
def ackPanelEnter():#________________________Panel Loader 2.._________________________________________________________:(
    LocX = mouseLocX.get_n() + viewPortX.get_n()
    for x in range(enterMinLocX.get_n(), enterMaxLocX.get_n()):#
        if x == LocX:#
            x = 1
            break
    LocY = mouseLocY.get_n() + viewPortY.get_n()
    for y in range(enterMinLocY.get_n(), enterMaxLocY.get_n()):#
        if y == LocY:#
            y = 1
            break
    if x + y == 2:#
        enterLoader.set_n(setMouse.get_n())
#
def ackPanelExit():##________________________Panel Loader  3...______##________________________________________________:(
    LocX = mouseLocX.get_n() + viewPortX.get_n()
    for x in range(exitMinLocX.get_n(), exitMaxLocX.get_n()):## 
        if x == LocX:##
            x = 1
            break
    LocY = mouseLocY.get_n() + viewPortY.get_n()
    for y in range(exitMinLocY.get_n(), exitMaxLocY.get_n()):##
        if y == LocY:##
            y = 1
            break
    if x + y == 2:##
        exitLoader.set_n(setMouse.get_n())
#
def ackPanelEnd():##________________________Panel Loader  4....______##________________________________________________:(
    LocX = mouseLocX.get_n() + viewPortX.get_n()
    for x in range(endMinLocX.get_n(), endMaxLocX.get_n()):## 
        if x == LocX:##
            x = 1
            break
    LocY = mouseLocY.get_n() + viewPortY.get_n()
    for y in range(endMinLocY.get_n(), endMaxLocY.get_n()):##
        if y == LocY:##
            y = 1
            break
    if x + y == 2:##
        endLoader.set_n(setMouse.get_n())
#
def ackPanelServer():##________________________Panel Loader  5.....______##________________________________________________:(
    LocX = mouseLocX.get_n() + viewPortX.get_n()
    for x in range(serverMinLocX.get_n(), serverMaxLocX.get_n()):## 
        if x == LocX:##
            x = 1
            break
    LocY = mouseLocY.get_n() + viewPortY.get_n()
    for y in range(serverMinLocY.get_n(), serverMaxLocY.get_n()):##
        if y == LocY:##
            y = 1
            break
    if x + y == 2:##
        serverLoader.set_n(setMouse.get_n())
#
def ackPanelMeshesRigs():##________________________Panel Loader  6......______##________________________________________________:(
    LocX = mouseLocX.get_n() + viewPortX.get_n()
    for x in range(meshesRigsMinLocX.get_n(), meshesRigsMaxLocX.get_n()):## 
        if x == LocX:##
            x = 1
            break
    LocY = mouseLocY.get_n() + viewPortY.get_n()
    for y in range(meshesRigsMinLocY.get_n(), meshesRigsMaxLocY.get_n()):##
        if y == LocY:##
            y = 1
            break
    if x + y == 2:##
        meshesRigsLoader.set_n(setMouse.get_n())
#
def ackPanelArena():##________________________Panel Loader  7.......______##________________________________________________:(
    LocX = mouseLocX.get_n() + viewPortX.get_n()
    for x in range(arenaMinLocX.get_n(), arenaMaxLocX.get_n()):## 
        if x == LocX:##
            x = 1
            break
    LocY = mouseLocY.get_n() + viewPortY.get_n()
    for y in range(arenaMinLocY.get_n(), arenaMaxLocY.get_n()):##
        if y == LocY:##
            y = 1
            break
    if x + y == 2:##
        arenaLoader.set_n(setMouse.get_n())  
#
def ackPanelClient():##________________________Panel Loader  7.......______##________________________________________________:(
    LocX = mouseLocX.get_n() + viewPortX.get_n()
    for x in range(clientMinLocX.get_n(), clientMaxLocX.get_n()):## 
        if x == LocX:##
            x = 1
            break
    LocY = mouseLocY.get_n() + viewPortY.get_n()
    for y in range(clientMinLocY.get_n(), clientMaxLocY.get_n()):##
        if y == LocY:##
            y = 1
            break
    if x + y == 2:##
        clientLoader.set_n(setMouse.get_n()) 
#
def ackPanelProject():##________________________Panel Loader  7.......______##________________________________________________:(
    LocX = mouseLocX.get_n() + viewPortX.get_n()
    for x in range(projectMinLocX.get_n(), projectMaxLocX.get_n()):## 
        if x == LocX:##
            x = 1
            break
    LocY = mouseLocY.get_n() + viewPortY.get_n()
    for y in range(projectMinLocY.get_n(), projectMaxLocY.get_n()):##
        if y == LocY:##
            y = 1
            break
    if x + y == 2:##
        projectLoader.set_n(setMouse.get_n()) 
