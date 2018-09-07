# !/usr/bin/env python .
# Created Tuseday, July 31, 2018 .
# Blender 2.79 wpremote.py
# 
# Last update :
def RemoteWp():#
    n = 0
    def func():#
        print('> RemoteWp', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setRemoteWp(wpremote):#
    remoteWp.set_n(wpremote)
def getRemoteWp(wpremote):#
    return remoteWp.get_n()
remoteWp = RemoteWp()
