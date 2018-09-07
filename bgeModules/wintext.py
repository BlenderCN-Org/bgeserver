# !/usr/bin/env python .
# Created Tuesday, September 4, 2018 .
# Blender 2.79 wintext.py
# 
# Last update :
# 
# 
#
#
#
#
#
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
class Loader:#
    def __init__(self):#
        self._x = None
    def getx(self):#
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Loader' property.")
loader = Loader()
#       

