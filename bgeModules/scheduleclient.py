# !/usr/bin/env python .
# Created Friday, August 10, 2018 .
# Blender 2.79 scheduleclient.py
# Schedule : time-management tool .
# Last update :
#
# Consists of a list of times at which possible tasks, events,
# or actions are intended to take place, or of a sequence of events .
#asmy.setx(1)
#asmy.getx()
#asmy.delx()
class Assembly:
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
asmy = Assembly()
class RigSched:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " 'Rig' property.")
schedrig = RigSched()
class MeshSched:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " 'Mesh' property.")
schedmesh = MeshSched()
class CamSched:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " 'Cam' property.")
schedcam = CamSched()
class ContSched:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " 'Cont' property.")
schedcont = ContSched()
