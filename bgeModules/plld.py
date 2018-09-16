# !/usr/bin/env python .
# Created Sunday, August 26, 2018 .
# Blender 2.79 plld.py
# Panel Loader Section  .
# Last update : Main, Server, Enter, Exit, Meshes&Rigs, Arena, Project, Client, End  .
###########################################
from bge import render
import ackpanel

#import threading
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
#____________________________________________
#               Panel Loader Section
#
# Main ' ' . 
# Server  ' ' . 
# Enter  ' ' .
# Exit  ' ' .
# Meshes Rigs  ' ' .
# Arena  ' ' .
# Project  ' ' .
# Client  ' ' .
# End  ' ' .
#
#____________________________________________
#               Panel Loader Section
#___________________________________________________________________________________________
def mainPanel():#____________________________________________________ Main Loader Section . ___________________________:(
    #escMain.set_n(1)
    #panelPlate.mouseEnter()
    #panelPlate.mouseExit()

    #setMouse.set_n(1)
    ackpanel.setMouse.setx(1)
    #mouseOpt.set_n(1)

    render.showMouse(1)
    #text.callServer()
#______________________________________________________________________________________________
def ackEnter():#_
    pass
#______________________________________________________________________________________________
def ackExit():#_
    pass
#______________________________________________________________________________________________
def ackServer():#_
    pass
#______________________________________________________________________________________________
def ackMeshesRigs():#_
    pass
#______________________________________________________________________________________________
def ackArena():#_
    pass
#______________________________________________________________________________________________
def ackProject():#_
    pass
#______________________________________________________________________________________________
def ackClient():#_
    pass
#______________________________________________________________________________________________
def ackEnd():#_
    pass
#______________________________________________________________________________________________
def ackContact():#_
    pass
