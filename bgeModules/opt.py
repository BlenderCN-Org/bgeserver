# !/usr/bin/env python .
# Created Tuesday, June 26, 2018 .
# Blender 2.79 opt.py
# 
# Last update :
def OptConsole():#
    n = 0
    def func():#
        print('> OptConsole ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setClient(opt):#
    optConsole.set_n(opt)
def getClient(opt):#
    return optConsole.get_n()
optConsole = OptConsole()
