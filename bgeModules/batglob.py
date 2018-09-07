# !/usr/bin/env python .
# Created Sunday, August 19, 2018 .
# Blender 2.79 batglob.py
# 
# Last update :
def MainBat():#
    n = 0
    def func():#
        print('> MainBat ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def end(batglob):#
    mainBat.set_n(batglob)
def start(batglob):#
    return mainBat.get_n()
mainBat = MainBat()
#######################
def Load():#
    n = 0
    def func():#
        print('> Load ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setload(batglob):#
    ld.set_n(batglob)
def load(batglob):#
    return ld.get_n()
ld = Load()
#######################
def Save():#
    n = 0
    def func():#
        print('> Save ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setsave(batglob):#
    sv.set_n(batglob)
def save(batglob):#
    return sv.get_n()
sv = Save()
#######################
def Access():#
    n = 0
    def func():#
        print('> Access ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setaccess(batglob):#
    acc.set_n(batglob)
def access(batglob):#
    return acc.get_n()
acc = Access()
