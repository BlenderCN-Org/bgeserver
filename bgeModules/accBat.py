# !/usr/bin/env python .
# Created Tuesday, August 21, 2018 .
# Blender 2.79 accBat.py
# 
# Last update :
#
#accbat.setx(1)
#accbat.getx()
#accbat.delx()
class AccBat:
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
accbat = AccBat()
class AccBatShowDisplay:
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
accdisplay = AccBatShowDisplay()
class AccBatArenaFloor:
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
accfloor = AccBatArenaFloor()
class AccBatPolygonFactory:
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
accpolyfact = AccBatPolygonFactory()

