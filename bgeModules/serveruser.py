# !/usr/bin/env python .
# Created Wednesday, August 29, 2018 .
# Blender 2.79 serveruser.py
# Library for New Created Functions
# Last update :
#
class Main:#
    def __init__(self):#
        self._x = None
    def getx(self):#
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Main' property.")
main = Main()
class MainReturns:#
    def __init__(self):#
        self._x = None
    def getx(self):#
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MainReturns' property.")
mainreturns = MainReturns()
class StateIdle:#
    def __init__(self):#
        self._x = None
    def getx(self):#
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MainReturns' property.")
idle = StateIdle()
