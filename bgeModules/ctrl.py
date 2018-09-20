# !/usr/bin/env python .
# Created Tuesday, June 26, 2018 .
# Blender 2.79 ctrl.py
# 
# Last update :
class ConsoleLedger:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ConsoleLedger' property.")
consoleledger = ConsoleLedger()
#consoleledger.setx(0)
class EscID:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'EscID' property.")
escid = EscID()
escid.setx(0) 
class ConsoleOpt:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ConsoleOpt' property.")
consoleopt = ConsoleOpt()
consoleopt.setx(0)
class CursorEntry:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'CursorEntry' property.")
cursorentry = CursorEntry()
#cursorentry.setx(0)
class UserClient:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'UserClient' property.")
userclient = UserClient()#
#userclient.setx(0)
class ClientConnected:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ClientConnected' property.")
clientconnected = ClientConnected()#
#clientconnected.setx(0) 
class UserRemote:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'UserRemote' property.")
userremote = UserRemote()#
#userremote.setx(0) 
class UserConnected:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'UserConnected' property.")
userconnected = UserConnected()#
#userconnected.setx(0)  
class ConsoleTextOpt:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ConsoleTextOpt' property.")
consoletextopt = ConsoleTextOpt()#
consoletextopt.setx(0) 
def CtrlConsole():#
    n = 0
    def func():#
        print('> CtrlConsole ', n) # cursorEntry
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
ctrlConsole = CtrlConsole()
#ctrlConsole.set_n(0) 
def setClient(ctrl):#
    ctrlConsole.set_n(ctrl)
def getClient(ctrl):#
    return ctrlConsole.get_n()

