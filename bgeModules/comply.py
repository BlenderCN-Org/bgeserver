# !/usr/bin/env python .
# Created Wednesday, August 22, 2018 .
# Blender 2.79 comply.py
# Justify argr.statements for idobjs.label . . .
# Last update 
#
##############################################
from bge import logic
##import math
class InputText:#

    def __init__(self):#

        self.scene = logic.getCurrentScene()
        self.text = self.scene.objects["RequestReturns"]


    def upDate(self):#

        if setwindow.getx() == 1:#
            self.popUp()
        else:#
            self.popDown()
            
    def popUp(self):#
        
        spawner = self.scene.objects["RequestReturnTarget"]
        self.text.position = spawner.worldPosition         

    def popDown(self):#

        spawner = self.scene.objects["ServerTextHolder"]
        self.text.position = spawner.worldPosition      

inputtext = InputText()
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
class SetWindow:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'SetWindow' property.")
setwindow = SetWindow()
class Visible:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Visible' property.")
visible = Visible()
