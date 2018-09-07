# !/usr/bin/env python .
# Created Friday, August 17, 2018 .
# Blender 2.79 objconfig.py
# 
# Last update :
###### ConfigObj  ######
def ConfigObj():#
    n = 0
    def func():#
        print('> ConfigObj ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def initend(objconfig):#
    configObj.set_n(objconfig)
def initstart(objconfig):#
    return configObj.get_n()
configObj = ConfigObj()
###################
def Mesh1Factory():#
    n = 0
    def func():#
        print('> Mesh1Factory ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def deletefactory(objconfig):#
    mesh1Factory.set_n(objconfig)
def loadfactory(objconfig):#
    return mesh1Factory.get_n()
mesh1Factory = Mesh1Factory()
###################
def PlayerCamera():#
    n = 0
    def func():#
        print('> PlayerCamera ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setmountcam(objconfig):#
    playerCamera.set_n(objconfig)
def getmountcam(objconfig):#
    return playerCamera.get_n()
playerCamera = PlayerCamera()
###################
def SpawnRig():#
    n = 0
    def func():#
        print('> SpawnRig ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setspawnrig(objconfig):#
    spawnRig.set_n(objconfig)
def getspawnrig(objconfig):#
    return spawnRig.get_n()
spawnRig = SpawnRig()
#####################
##### ControlsRig #####
def ControlsRig():#
    n = 0
    def func():#
        print('> ControlsRig ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setcontrols(objconfig):#
    controlsRig.set_n(objconfig)
def getcontrols(objconfig):#
    return controlsRig.get_n()
controlsRig = ControlsRig()
#####################
