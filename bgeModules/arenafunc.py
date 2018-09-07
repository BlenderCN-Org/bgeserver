# !/usr/bin/env python .
# Created Wednesday, August 23, 2018 .
# Blender 2.79 arenafunc.py
# 
# Last update 
#
#########################
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
#########################


