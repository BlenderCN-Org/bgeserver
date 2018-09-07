# !/usr/bin/env python .
# Created Friday, June 22, 2018 .
# Blender 2.79 gladhands.py
# 
# Last update :
def Glad():#
    n = 0
    def func():#
        print('> Glad ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def listen(gladhands):#
    glad.set_n(gladhands)
def quiet(gladhands):#
    return glad.get_n()    
glad = Glad()
