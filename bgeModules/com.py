# !/usr/bin/env python .
# Created Wednesday, August 8, 2018 .
# Blender 2.79 com.py
# 
# Last update :
def ComPro():#
    n = 0
    def func():#
        print('> ComPro', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setCom(com):#
    comPro.set_n(com)
def getCom(com):#
    return comPro.get_n()
comPro = ComPro()
