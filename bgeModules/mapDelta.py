# !/usr/bin/env python .
# Created Tuesday, August 21, 2018 .
# Blender 2.79 mapDelta.py
# 
# Last update :
#
#accbat.setx(1)
#accbat.getx()
#accbat.delx()
class MapMain:
    def __init__(self):
        self._x = None
    #c.x will invoke the getter.
    def getx(self):
        return self._x
    #c.x = value will invoke the setter .
    def setx(self, value):
        self._x = value
    #del c.x the deleter.
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, "I'm the 'x' property.")
main = MapMain()
class MapRig:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ShowDisplay' property.")
rig = MapRig()
class MapMesh:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, ">>> 'ArenaFloor' property.")
mesh = MapMesh()
class MapCam:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'PolygonFactory' property.")
cam = MapCam()
class MapCont:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'PolygonFactory' property.")
cont = MapCont()
class MapMax:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'PolygonFactory' property.")
mapmax = MapMax()
class MapMin:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'PolygonFactory' property.")
mapmin = MapMin()
class MapChange:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MapChange' property.")
deltachange = MapChange()
class ServerStart:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MapChange' property.")
servstart = ServerStart()
