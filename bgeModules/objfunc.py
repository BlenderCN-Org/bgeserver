# !/usr/bin/env python .
# Created Friday, August 17, 2018 .
# Blender 2.79 objfunc.py
# 
# Last update :
###### MainObj  ######
def MainObj():#
    n = 0
    def func():#
        print('> MainObj ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def end(objfunc):#
    mainObj.set_n(objfunc)
def start(objfunc):#
    return mainObj.get_n()
mainObj = MainObj()
###### ResetRig #######
def ResetRig():#
    n = 0
    def func():#
        print('> ResetRig ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setrig(objfunc):#
    resetRig.set_n(objfunc)
def getrig(objfunc):#
    return resetRig.get_n()
resetRig = ResetRig()
##### ResetMesh #####
def ResetMesh():#
    n = 0
    def func():#
        print('> ResetMesh ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setmesh(objfunc):#
    resetMesh.set_n(objfunc)
def getmesh(objfunc):#
    return resetMesh.get_n()
resetMesh = ResetMesh()
##### RigControls #####
def RigControls():#
    n = 0
    def func():#
        print('> RigControls ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setkeyboard(objfunc):#
    rigControls.set_n(objfunc)
def getkeyboard(objfunc):#
    return rigControls.get_n()
rigControls = RigControls()
##### CameraMount #####
def CameraMount():#
    n = 0
    def func():#
        print('>CameraMount ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setcam(objfunc):#
    cameraMount.set_n(objfunc)
def getcam(objfunc):#
    return cameraMount.get_n()
cameraMount  = CameraMount()
#####################
