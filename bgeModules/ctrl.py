# !/usr/bin/env python .
# Created Tuesday, June 26, 2018 .
# Blender 2.79 ctrl.py
# 
# Last update :
def CtrlConsole():#
    n = 0
    def func():#
        print('> CtrlConsole ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setClient(ctrl):#
    ctrlConsole.set_n(ctrl)
def getClient(ctrl):#
    return ctrlConsole.get_n()
ctrlConsole = CtrlConsole()
