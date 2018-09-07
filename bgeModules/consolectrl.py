# !/usr/bin/env python .
# Created Friday, August 10, 2018 .
# Blender 2.79 consolectrl.py
# 
# Last update :
def ConPro():#
    n = 0
    def func():#
        print('> ConPro', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setConsole(consolectrl):#
    conPro.set_n(consolectrl)
def getConsole(consolectrl):#
    return conPro.get_n()
conPro = ConPro()
