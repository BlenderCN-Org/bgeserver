# !/usr/bin/env python .
# Created Tuesday, June 26, 2018 .
# Blender 2.79 pan.py
# 
# Last update :
def SingleMulit():#
    n = 0
    def func():#
        print('> SingleMulit ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setClient(pan):#
    singleMulit.set_n(pan)
def getClient(pan):#
    return singleMulit.get_n()
singleMulit = SingleMulit()
