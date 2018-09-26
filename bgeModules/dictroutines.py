# !/usr/bin/env python .
# Created Saturday, September 22, 2018 .
# Blender 2.79 dictroutines.py
# 
# Last update :
#import 
dict_pack = []
list_pack = []
def Assets(listing_key):
    listing = {
        0: 'jawbite',
        1: 'assets',
        2: 'assets',
        3: 'assets',
        4: 'assets',
        5: 'assets',
        6: 'assets',
        }
    return listing[listing_key]

def dict_Routine():
    for k in range(7):
        dict_pack = Assets(k)
        list_pack.append(dict_pack)
    return list_pack
