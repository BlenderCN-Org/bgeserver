# !/usr/bin/env python .
# Created Tuesday, June 26, 2018 .
# Blender 2.79 esc.py
# 
# Last update :
def Escape():#
    n = 0
    def func():#
        print('> Escape ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setEsc(esc):#
    escape.set_n(esc)
def getEsc(esc):#
    return escape.get_n()
escape = Escape()
