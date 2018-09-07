# !/usr/bin/env python .
# Created Tuesday, July 3, 2018 .
# Blender 2.79 soundctrl.py
# 
# Last update :
def SoundControl():#
    n = 0
    def func():#
        print('> SoundControl ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def sound(soundctrl):#
    return soundControl.get_n()
def soundoff(soundctrl):#
    soundControl.set_n(soundctrl)
soundControl = SoundControl()
