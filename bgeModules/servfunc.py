# !/usr/bin/env python .
# Created Thursday, August 30, 2018 .
# Blender 2.79 servfunc.py
# 
# Last update :
import idserv
import comply
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
class MSG:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MSG' property.")
msg = MSG()
def loadfunction():#
   
    if idserv.main.getx() == 1:#
        idserv.main.delx()
        data = {'house':'5', 'name': 'Start Server ', 'town': 'Stephenville'}# 
        idserv.servlocal.setx(1)        
        return data# 

    if idserv.msg.getx() == 1:#
        idserv.msg.delx()
        data = {'house':'5', 'name': 'MSG off ', 'town': 'Stephenville'}# 
        comply.visible.setx(1)        
        return data# 
