# !/usr/bin/env python .
# Created Tuesday, August 21, 2018 .
# Blender 2.79 libmenu.py
# 
# Last update :
#
class  Menu:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Menu.lib")
menu = Menu()
