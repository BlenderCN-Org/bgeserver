# !/usr/bin/env python .
# Created Tuesday, June 26, 2018 .
# Blender 2.79 log.py
# 
# Last update :
def LogConsole():#
    n = 0
    def func():#
        print('> LogConsole ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setClient(log):#
    logConsole.set_n(log)
def getClient(log):#
    return logConsole.get_n()
logConsole = LogConsole()
