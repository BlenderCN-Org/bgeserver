# !/usr/bin/env python .
# Created Tuesday, June 26, 2018 .
# Blender 2.79 request.py
# 
# Last update :
def ConsoleReturns():#
    n = 0
    def func():#
        print('> ConsoleReturns ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setRequest(request):#
    consoleReturns.set_n(request)
def getRequest(request):#
    return consoleReturns.get_n()
consoleReturns = ConsoleReturns()
