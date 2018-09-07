# !/usr/bin/env python .
# Created Saturday, June 30, 2018 .
# Blender 2.79 arena.py 
# 
# Last update : 
def Render():#
    n = 0
    def func():#
        print('> Render', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def onArena(arena):#
    return render.get_n()
def offArena(arena):#
    render.set_n(arena)
render = Render()    
