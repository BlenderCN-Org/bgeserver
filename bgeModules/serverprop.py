# !/usr/bin/env python .
# Created Friday, August 10, 2018 .
# Blender 2.79 serverprop.py
# 
# Last update :
#
class C:
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
        gstar.x=0
    x = property(getx, setx, delx, "I'm the 'x' property.")
gstar =C()
