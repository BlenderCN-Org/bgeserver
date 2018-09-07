# !/usr/bin/env python .
# Created Saturday, August 11, 2018 .
# Blender 2.79 dictrig.py
# 
# Last update :
dict_pack = []
list_pack = []
import configdeltas
def Rig(listing_key):#
    listing = {
        0: '_mm_',
        1: '_init_',
        2: '_id_',
        3: '_dict_',
        4: '_config_' ,
        5: '_bat_',
        6: '_lib_' ,
    }
    return listing[listing_key]#
def dict_Rig():#_.........
    configdeltas.deleteRig(1)
    for k in range(7):#_____________________
        dict_pack = Rig(k)#
        list_pack.append(dict_pack)
    return list_pack
