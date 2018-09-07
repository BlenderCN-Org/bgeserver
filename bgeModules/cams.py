# !/usr/bin/env python .
# Created Wednesday, June 12, 2018 .
# Blender 2.79 cams.py
# 
# Last update :
def Camera():#
    n = 0
    def func():#
        print('> Camera ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
