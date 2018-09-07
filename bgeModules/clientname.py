# !/usr/bin/env python .
# Created Saturday, July 19, 2018 .
# Blender 2.79 clientname.py
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
def Position():#
    n = 0
    def func():#
        print('> Position', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def enterName(clientname):#
    name.set_n(clientname)
def returnName(clientname):#
    return name.get_n()
def enterPos(clientname):#
    position.set_n(clientname)
def returnPos(clientname):#
    return position.get_n()
name = Name()
position = Position()
