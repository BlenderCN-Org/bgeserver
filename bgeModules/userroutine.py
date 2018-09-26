# !/usr/bin/env python .
# Created Tuesday, August 21, 2018 .
# Blender 2.79 userroutine.py
# 
# Last update :
#
import iduser
import mmenu
import batmenu
class  Main:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Routine")
main = Main()

def loadroutine():#
    func_input = iduser.initUserEnd(iduser)   

    if func_input == 'jawbite':#
        data = {'house':'5', 'name': 'jawbite', 'town': 'Stephenville'}# 
        mmenu.routine.delx()
        batmenu.menu.setx(1)
        return data# 
    
    else:#
        data = {'house':'empty', 'name': 'loadroutine', 'town': 'empty'}# 
        return data#  
