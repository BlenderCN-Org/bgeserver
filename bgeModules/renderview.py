# !/usr/bin/env python .
# Created Wednesday,  June 20,  2018  .
# Blender 2.79 renderview.py
# 
# Last update :
def SingleView():#
    n = 0
    def func():#
        print('> SingleView ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def MultiView():#
    n = 0
    def func():#
        print('> MultiView ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setSingle(renderview):#
    singleView.set_n(renderview)
def getSingle(renderview):#
    return singleView.get_n()
def setMulti(renderview):#
    multiView.set_n(renderview)
def getMulti(renderview):#
    return multiView.get_n()
singleView = SingleView()
multiView = MultiView()
