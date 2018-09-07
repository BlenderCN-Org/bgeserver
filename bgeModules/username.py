# !/usr/bin/env python .
# Created Saturday, July 14, 2018 .
# Blender 2.79 username.py
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
def enterName(username):#
    name.set_n(username)
def returnName(username):#
    return name.get_n()
name = Name()
