# !/usr/bin/env python .
# Created Wednesday, August 23, 2018 .
# Blender 2.79 polyfactory.py
# 
# Last update 
#
from bge import logic
scene = logic.getCurrentScene()
#########################
##if mesh1Factory.get_n() == 0:#
##    spawner = scene.objects["SuzannesPoint"]
##    mesh1 = scene.addObject("Suzanne", spawner)
##    mesh1Factory.set_n(1)
##    ''' Blender Stock Suzanne Friend .'''
##if mesh2Factory.get_n() == 0:#
##    spawner = scene.objects["Suzannes2Point"]
##    mesh1 = scene.addObject("SuzanneRemote", spawner)
##    mesh2Factory.set_n(1)
##    ''' PacMan Build . '''
##if mesh3Factory.get_n() == 0:#
##    spawner = scene.objects["SpawnerPacMan"]
##    mesh1 = scene.addObject("MeshBuild", spawner)
##    mesh2 = scene.addObject("TopJaw", spawner)
##    mesh3 = scene.addObject("BottomJaw", spawner)
##    self.closeJaws()
##    mesh3Factory.set_n(1)
##if mesh4Factory.get_n() == 0:#
##    spawner = scene.objects["SpawnerPacMan"]
##    mesh1 = scene.addObject("SuzannesBaby2", spawner)
##    mesh4Factory.set_n(1)
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
class Suzanne:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
        spawner = scene.objects["SuzannesPoint"]
        mesh1 = scene.addObject("Suzanne", spawner)
    def delx(self):
        del self._x
        self._x = None
        obj1 = scene.objects["Suzanne"]
        obj1.endObject()
    x = property(getx, setx, delx, " >>> 'Suzanne' property.")
suzanne = Suzanne()
class SuzanneRemote:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
        spawner = scene.objects["Suzannes2Point"]
        mesh1 = scene.addObject("SuzanneRemote", spawner)
    def delx(self):
        del self._x
        self._x = None
        obj1 = scene.objects["SuzanneRemote"]
        obj1.endObject()
    x = property(getx, setx, delx, " >>> 'SuzanneRemote' property.")
remote = SuzanneRemote()
class MeshBuild:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
        spawner = scene.objects["SpawnerPacMan"]
        mesh1 = scene.addObject("MeshBuild", spawner)
        mesh2 = scene.addObject("TopJaw", spawner)
        mesh3 = scene.addObject("BottomJaw", spawner)
        #self.closeJaws()
    def delx(self):
        del self._x
        self._x = None
        obj1 = scene.objects["MeshBuild"] 
        obj2 = scene.objects["TopJaw"] 
        obj3 = scene.objects["BottomJaw"]
        obj1.endObject()
        obj2.endObject()
        obj3.endObject()
    x = property(getx, setx, delx, " >>> 'MeshBuild' property.")
pacman = MeshBuild()
class SuzannesBaby2:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
        spawner = scene.objects["SpawnerPacMan"]
        mesh1 = scene.addObject("SuzannesBaby2", spawner)
    def delx(self):
        del self._x
        self._x = None
        obj1 = scene.objects["SuzannesBaby2"] 
        obj1.endObject()
    x = property(getx, setx, delx, " >>> 'Main' property.")
baby = SuzannesBaby2()
