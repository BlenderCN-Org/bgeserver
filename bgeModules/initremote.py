# !/usr/bin/env python .
# Created Friday, June 13, 2018 .
# Blender 2.79 initremote.py
# 
# Last update :
def NameRemote():#
    n = 0
    def func():#
        print('> NameRemote', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setEnter(initremote):#
    nameRemote.set_n(initremote)
def getEnter(initremote):#
    return nameRemote.get_n()
nameRemote = NameRemote()
