# !/usr/bin/env python .
# Created Saturday, August 11, 2018 .
# Blender 2.79 dictserver.py
# 
# Last update :
import filesys
import idserv
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
def Commands(listing_key):#
    listing = {
        0: 'gstar',
        1: 'time',
        2: 'dir',
        3: 'upload',
        4: 'download' ,
        5: 'show list',
        6: 'cd/',
        7: 'server name',
        8: 'show dir',
        9: 'list',
        10: 'serverlist',
        11: 'module',
        12: 'socket size',
        13: 'get file size',
        14: 'set codec',
        15: 'live mic',
        16: 'server*stream',
        17: 'recorder off',
        18: 'soundlist',
        }
    return listing[listing_key]#
def dict_Global():#_.........
    filesys.main.setx(1)
    for k in range(19):#_____________________
        dict_pack = Commands(k)#
        list_pack.append(dict_pack)
    return list_pack
def Assets(listing_key):#
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
def dict_Local():#_.........
    idserv.main.setx(1)
    for k in range(7):#_____________________
        dict_pack = Assets(k)#
        list_pack.append(dict_pack)
    return list_pack        
