# !/usr/bin/env python .
# Created Wednesday, August 22, 2018 .
# Blender 2.79 incident.py
# Justify comply with  incident for argr.statements .
# Last update 
#
####################################################
#from bge import logic
#import math
import comply
import wintext
dict_pack = []
list_pack = []
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
class Time:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Time' property.")
time = Time()
class Gstar:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Gstar' property.")
gstar = Gstar()
class ShowDir:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ShowDir' property.")
showdir = ShowDir()
class Search:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Search' property.")
search = Search()
class TextWindow:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'TextWindow' property.")
textwindow = TextWindow()
class CmdPass:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'CmdPass' property.")
cmdpass = CmdPass()
class Mark:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Mark' property.")
mark = Mark()
##
#

#________________________________CheckDict
class CheckDict:#

    def __init__(self):#

        self.default = ['gstar', 'time', 'show dir', 'dir',  'show list', 'server name',
                        'list', 'serverlist', 'module', 'recorder off', 'soundlist' ]

        self.invalid = ['upload', 'download', 'cd/',
                        'socket size', 'get file size', 'set codec', 'live mic', ]

    def seekfunc(self):#
        value = 0
        seek = search.getx()
        if seek in self.invalid:#
            value = 1
            
        comply.setwindow.setx(value)
         
checkdict = CheckDict()     
##
#

#_________________________________ReplyReturns
def ReplyReturns(listing_key):#
    listing = {
        0: 'start',
        1: 'msg',
        2: 'empty',
        3: 'empty',
        4: 'empty',
        5: 'empty',
        6: 'empty',
        }
    return listing[listing_key]#
def dict_Replies():#_.........
    idserv.main.setx(1)
    for k in range(7):#_____________________
        dict_pack = ReplyReturns(k)#
        list_pack.append(dict_pack)
    return list_pack    
##
#

###############################################
class CheckReply:#

    def __init__(self):#

        self.default = ['>...File Label___name.*', '> Enter file size * >',
                        'Request file size Label *', '>>> * * Enter time for Recording . * *',
                        'Change Directory', '> Invalid Selection <', '>Ready for Upload ://',
                        '>>> * Live Mic * > File : Label.wav']

        self.invalid = ['live mic']

    def seekincident(self):#
        value = 0
        seek = mark.getx()
        if seek in self.default :#
            value = 1
        textwindow.setx(value)
         
checkreply = CheckReply()    
#checkreply.seekincident()
