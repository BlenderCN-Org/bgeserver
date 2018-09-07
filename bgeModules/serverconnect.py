# !/usr/bin/env python .
# Created Friday, June 22, 2018 .
# Blender 2.79 serverconnect.py
# 
# Last update :
def ConnectServer():#
    n = 0
    def func():#
        print('> ConnectServer ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def Disconnect(serverconnect):#
    connectServer.set_n(serverconnect)
def Connect(serverconnect):#
    return connectServer.get_n()
connectServer = ConnectServer()
