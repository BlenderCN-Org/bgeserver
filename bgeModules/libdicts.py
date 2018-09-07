# !/usr/bin/env python .
# Created Tuesday, August 21, 2018 .
# Blender 2.79 libdicts.py
# 
# Last update :
#
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
    x = property(getx, setx, delx, " >>> 'ShowDisplay' property.")
main = Main()
