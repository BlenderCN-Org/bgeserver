# !/usr/bin/env python .
# Created Monday, August 27, 2018 .
# Blender 2.79 setupfilesys.py
# 
# Last update : 
###########################################
##########################################
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
############
#
############
class NameLabel:#
    def __init__(self):#
        self._x = None
    def getx(self):#
        assets.namelabel()
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'NameLabel' property.")
namelabel = NameLabel()
########
#
#############
class StartServer:#
    def __init__(self):#
        self._x = None
    def getx(self):#
        assets.startserver()
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'StartServer' property.")
startserver = StartServer()
########
#
#############
class FileSystem:#
    def __init__(self):#
        self._x = None
    def getx(self):#
        assets.filesystem()
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Main' property.")
filesystem = FileSystem()
########
#
#############
class ServerError(Exception):#
    def __init__(self, message):#
        self.message = message
#
class Assets:#_____________________:(

    def __init__(self):#

        self.load = []

    def startserver(self):#

        print(' >>> startserver <<< ')       

    def namelabel(self):#_________________________________________________:(

        print(' >>> namelabel <<< ')

    def filesystem(self):#_________________________________________________:(

        print(' >>> filesystem <<< ')
        self.returns()

    def returns(self):#_________________________________________________:(

        print(' >>> returns <<< ')
assets  = Assets()
