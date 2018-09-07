# !/usr/bin/env python .
# Created Sunday, August 19, 2018 .
# Blender 2.79 configglob.py
# 
# Last update :
def MainConfig():#
    n = 0
    def func():#
        print('> MainConfig ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def end(configglob):#
    mainConfig.set_n(configglob)
def start(configglob):#
    return mainConfig.get_n()
mainConfig = MainConfig()
########################
def RigFigure():#
    n = 0
    def func():#
        print('> RigFigure ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setrig(configglob):#
    rigFigure.set_n(configglob)
def getrig(configglob):#
    return rigFigure.get_n()
rigFigure = RigFigure()
#############################
def MeshFigure():#
    n = 0
    def func():#
        print('> MeshFigure ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setmesh(configglob):#
    meshFigure.set_n(configglob)
def getmesh(configglob):#
    return meshFigure.get_n()
meshFigure = MeshFigure()
#############################
def CameraFigure():#
    n = 0
    def func():#
        print('> CameraFigure ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setcamera(configglob):#
    cameraFigure.set_n(configglob)
def getcamera(configglob):#
    return cameraFigure.get_n()
cameraFigure = CameraFigure()
#############################
def ControlsFigure():#
    n = 0
    def func():#
        print('> ControlsFigure ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setcontrols(configglob):#
    controlsFigure.set_n(configglob)
def getcontrols(configglob):#
    return controlsFigure.get_n()
controlsFigure = ControlsFigure()
#########################
# configglob.end(1)
# configglob.start(configglob)
# configglob.setrig(1)
# configglob.getrig(configglob)
# configglob.setmesh(1)
# configglob.getmesh(configglob)
# configglob.setcamera(1)
# configglob.getcamera(configglob)
# configglob.setcontrols(1)
# configglob.getcontrols(configglob)
