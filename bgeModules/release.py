# !/usr/bin/env python .
# Created Saturday, July 14, 2018 .
# Blender 2.79 release.py
# 
# Last update :
def RemoteCtrl():#
    n = 0
    def func():#
        print('> RemoteCtrl ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def enterRelease(release):#
    remoteCtrl.set_n(release)
def returnRelease(release):#
    return remoteCtrl.get_n()
remoteCtrl = RemoteCtrl()
