# !/usr/bin/env python .
# Created Friday, August 24, 2018 .
# Blender 2.79 mapscreen.py
# 
# Last update 
#
####################################################
from bge import types, logic, render
render.showMouse(1)
####################################################
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
'''' Loader1 and Loader2 are the "enter"; "exit"; detector.Locators : >>>*__init__*<<< main.MenuPanels  .                            '''
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .:(
        cont = self.controllers[0]
        self.sen = cont.sensors

        self.main = self.state_idle

    def _getClickAndHit(self):#

        return (self.sen["leftclick"].positive,
                self.sen["mouseover"].hitObject)




#____________________________________________________________________________________________________________________:(
#
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
