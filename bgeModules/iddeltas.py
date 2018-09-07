# !/usr/bin/env python .
# Created Tuesday, August 14, 2018 .
# Blender 2.79 iddeltas.py
# 
# Last update :
##import iduser
##pre_id = iduser.initUserEnd(iduser)
def ComDeltas():#
    n = 0
    def func():#
        print('> ComDeltas', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def startFunc(iddeltas):#
    comDeltas.set_n(iddeltas)
def endFunc(iddeltas):#
    return comDeltas.get_n()
comDeltas = ComDeltas()
