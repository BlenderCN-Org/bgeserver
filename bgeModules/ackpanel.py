# !/usr/bin/env python .
# Created Sunday, August 26, 2018 .
# Blender 2.79 ackpanel.py
# 
# Last update 
#
###########################################
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
###########################################
class Loader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Loader' property.")
loader = Loader()
########################
class Index:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Index' property.")
index = Index()
##########################
#
##########################
#
dict_pack = []
list_pack = []
getpanel = []
#
########################
def Panel(listing_key):#
    listing = {
        0: 'ackMain',
        1: 'ackEnter',
        2: 'ackExit',
        3: 'ackServer',
        4: 'ackMeshesRigs',
        5: 'ackArena',
        6: 'ackProject',
        7: 'ackClient' ,
        8: 'ackEnd',
        9: 'ackContact',
    }
    return listing[listing_key]#
def dict_Panel():#_.........
    for k in range(10):#_____________________
        dict_pack = Panel(k)#
        list_pack.append(dict_pack)
    return list_pack
########################
#
############################
class MouseLocX:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MouseLocX' property.")
mouseLocX = MouseLocX()
mouseLocX.setx(1)
############################
class MouseLocY:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MouseLocY' property.")
mouseLocY = MouseLocY()
mouseLocY.setx(1)
########################
#
############################
class MinLocX:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MinLocX' property.")
minLocX = MinLocX()
minLocX.setx(1) 
############################
class MaxLocX:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MaxLocX' property.")
maxLocX = MaxLocX()
maxLocX.setx(1) 
############################
class MinLocY:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MinLocY' property.")
minLocY = MinLocY()
minLocY.setx(1) 
############################
class MaxLocY:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MaxLocY' property.")
maxLocY = MaxLocY()
maxLocY.setx(1) 
########################
#
############################
class ViewPortX:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ViewPortX' property.")
viewPortX = ViewPortX()
viewPortX.setx(1)
############################
class ViewPortY:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ViewPortY' property.")
viewPortY = ViewPortY()
viewPortY.setx(1)
########################
#
############################
############################
class SetMouse:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'SetMouse' property.")
setMouse = SetMouse()
########################
#
############################
###########################
listing = {'ackMain':'0', 'ackEnter':'1', 'ackExit':'2', 'ackServer':'3',
           'ackMeshesRigs':'4' , 'ackArena':'5',
           'ackClient':'6', 'ackProject':'7', 'ackEnd':'8', 'ackContact':'p'}

###########################
def find_command(map, command):#
    if command in map:#
        main.setx(1)
        return map[command]
    else:#
        main.delx()
        index.delx()
        return "no deltas"

def findpanel():#
    listing['_found'] = find_command
    func_input = index.getx()
    return find_command(listing,(func_input))
############################
def ackLoader():#________________________Loader Model Final _________________________________________________________:(
    LocX = int(mouseLocX.getx() + viewPortX.getx())
    for x in range(minLocX.getx(), maxLocX.getx()):#
        if x == LocX:#
            x = 1
            break
    LocY = int(mouseLocY.getx() + viewPortY.getx())
    for y in range(minLocY.getx(), maxLocY.getx()):#
        if y == LocY:#
            y = 1
            break
    if x + y == 2:#
        loader.setx(setMouse.getx())

    ########################


    
