# !/usr/bin/env python .
# Created Sunday, August 26, 2018 .
# Blender 2.79 plld.py
# Panel Loader Section  .
# Last update : Main, Server, Enter, Exit, Meshes&Rigs, Arena, Project, Client, End  .
###########################################
from bge import logic, render
import math
import ackpanel
import config
import threading
import mouseclick
#import filesys
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
class MainLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MainLoader' property.")
mainloader = MainLoader()
#________________________
class EnterLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'EnterLoader' property.")
enterloader = EnterLoader()
#________________________
class ExitLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ExitLoader' property.")
exitloader = ExitLoader()
#________________________
class ServerLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ServerLoader' property.")
serverloader = ServerLoader()
#________________________
class MeshesRigsLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MeshesRigsLoader' property.")
meshesrigsloader = MeshesRigsLoader()
#________________________
class ArenaLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ArenaLoader' property.")
arenaloader = ArenaLoader()
#________________________
class ProjectLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ProjectLoader' property.")
projectloader = ProjectLoader()
#________________________
class ClientLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ClientLoader' property.")
clientloader = ClientLoader()
#________________________
class EndLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'EndLoader' property.")
endloader = EndLoader()
#________________________
def beforeYouGo():#__________________________Client Off___________________________:(
    self.camera90()
    print(' >>> Contact Server ')
    scene = logic.getCurrentScene()
    spawnArea = scene.objects["Camera.001"]        
    spawner = scene.objects["BeforeYouGo"]
    spawnArea.position = spawner.worldPosition  
def camera90():#_____________________________:(
    Zangle = 90
    scene = logic.getCurrentScene()
    camera = scene.objects["Camera.001"]#
    xyz = camera.worldOrientation.to_euler()
    xyz[2] = math.radians(Zangle)
    camera.localOrientation = xyz.to_matrix() 
#____________________________________________
#               Panel Loader Section
#___________________________________________________________________________________________
def mainPanel():#____________________________________________________ Main Loader Section . ___________________________:(
    mainloader.setx(1)
    #panelPlate.mouseEnter()
    #panelPlate.mouseExit()
    #ackpanel.setMouse.setx(1)
    render.showMouse(1)
#______________________________________________________________________________________________
def ackEnter():#_
    enterloader.setx(1)

    mouseclick.rtclick.setx(1)

    render.showMouse(1)
#______________________________________________________________________________________________
def ackExit():#_
    exitloader.setx(1)
#______________________________________________________________________________________________
def ackServer():#_
    serverloader.setx(1)
#______________________________________________________________________________________________
def ackMeshesRigs():#_
    meshesrigsloader.setx(1)
#______________________________________________________________________________________________
def ackArena():#_
    arenaloader.setx(1)
#______________________________________________________________________________________________
def ackProject():#_
    projectloader.setx(1)
#______________________________________________________________________________________________
def ackClient():#_
    clientloader.setx(1)
#______________________________________________________________________________________________
def ackEnd():#_
    endloader.setx(1)
#______________________________________________________________________________________________
def ackContact():#_
    pass
