# !/usr/bin/env python .
# Created Saturday, August 11, 2018 .
# Blender 2.79 dictchange.py
# 
# Last update :
import configdeltas
dict_pack = []
list_pack = []
def Assets(listing_key):#
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
#
def dict_Change():#_.........
    configdeltas.deletechange(1)
    for k in range(19):#_____________________
        dict_pack = Assets(k)#
        list_pack.append(dict_pack)
    return list_pack
