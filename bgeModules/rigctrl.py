# !/usr/bin/env python .
# Created Tuesday, August 21, 2018 .
# Blender 2.79 rigctrl.py
# 
# Last update :
#
#asmy.setx(1)
#asmy.getx()
#asmy.delx()
class  RigCtrl:
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
rigCtrl = RigCtrl()

