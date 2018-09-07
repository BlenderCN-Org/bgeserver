# !/usr/bin/env python .
# Created Tuesday, June 26, 2018 .
# Blender 2.79 rtn.py
# 
# Last update :
def OptReturn():#
    n = 0
    def func():#
        print('> OptReturn ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
optReturn = OptReturn()
def setCtrl(opt):#
    optReturn.set_n(opt)
def getCtrl(opt):#
    return optReturn.get_n()

