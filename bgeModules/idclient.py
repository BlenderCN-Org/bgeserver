# !/usr/bin/env python .
# Created Saturday, June 23, 2018 .
# Blender 2.79 idclient.py
# 
# Last update :
def Disconnect():#
    n = 0
    def func():#
        print('> Disconnect', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def ReturnAddress():#
    n = 0
    def func():#
        print('> ReturnAddress', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setLogOff(idclient):#
    disconnect.set_n(idclient)
def getLogOff(idclient):#
    return disconnect.get_n()
def setRaddr(idclient):#
    returnAddress.set_n(idclient)
def getRaddr(idclient):#
    return returnAddress.get_n()
disconnect = Disconnect()
returnAddress = ReturnAddress()
