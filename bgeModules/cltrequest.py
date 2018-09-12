# !/usr/bin/env python .
# Created Monday, August 27, 2018 .
# Blender 2.79 cltrequest.py
# 
# Last update :
#
import configdeltas
import iduser
dict_pack = []
list_pack = []
key_pack = []
class Alfa:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Alfa' property.")
alfa = Alfa()
def Request(listing_key):#
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
def loadfunction():#_.........
    configdeltas.deleterequest(1)
    for k in range(19):#_____________________
        dict_pack = Request(k)#
        list_pack.append(dict_pack)
    return list_pack
###########################
listing = {'gstar':'0', 'time':'1', 'dir':'2', 'upload':'3', 'download':'4' , 'show list':'5',
           'cd/':'6', 'server name':'7', 'show dir':'8', 'list':'9', 'serverlist':'10',
           'module':'11', 'socket size':'12', 'get file size':'13', 'set codec':'14', 'live mic':'15',
           'server*stream':'16', 'recorder off':'17', 'soundlist':'18'}
###########################
def find_command(map, command):#
    if command in map:#
        return map[command]
    else:#
        return "Not found"

def findfunc():#
    listing['_found'] = find_command
    func_input = iduser.initUserEnd(iduser) 
    return find_command(listing,(func_input))    


