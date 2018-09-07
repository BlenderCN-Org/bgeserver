# !/usr/bin/env python .
# Created Tuesday, June 26, 2018 .
# Blender 2.79 text.py
# 
# Last update :
def InputConsole():#
    n = 0
    def func():#
        print('> InputConsole ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setConsole(text):#
    inputConsole.set_n(text)
def getConsole(text):#
    text = inputConsole.get_n()
    return text
inputConsole = InputConsole()
