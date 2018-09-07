# !/usr/bin/env python .
# Created Saturday, June 23, 2018 .
# Blender 2.79 initenter.py
# 
# Last update :
def NameEnter():#
    n = 0
    def func():#
        print('> NameEnter', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setEnter(initenter):#
    nameEnter.set_n(initenter)
def getEnter(initenter):#
    return nameEnter.get_n()
nameEnter = NameEnter()
