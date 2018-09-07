# !/usr/bin/env python .
# Created Friday, June 29, 2018 .
# Blender 2.79 remotename.py
# 
# Last update :
def Name():#
    n = 0
    def func():#
        print('> Name', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def enterName(remotename):#
    name.set_n(remotename)
def returnName(remotename):#
    return name.get_n()
name = Name()
