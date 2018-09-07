# !/usr/bin/env python .
# Created Friday, June 22, 2018 .
# Blender 2.79 userpass.py
# 
# Last update :
def SinglePass():#
    n = 0
    def func():#
        print('> SinglePass ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def MultiPass():#
    n = 0
    def func():#
        print('> MultiPass ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setSingle(single):#
    singlePass.set_n(single)
def getSingle(single):#
    return singlePass.get_n()
singlePass = SinglePass()
def setMulti(multi):#
    multiPass.set_n(multi)
def getMulti(multi):#
    return multiPass.get_n()
multiPass = MultiPass()
