# !/usr/bin/env python .
# Created Monday, August 13, 2018 .
# Blender 2.79 iduser.py
#  .
# Last update :
def DeltasUserFunc():#
    n = 0
    def func():#
        print('> DeltasUserFunc ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def endFuncProc(iduser):#
    deltasUserFunc.set_n(iduser)
def startFuncProc(iduser):#
    return deltasUserFunc.get_n()
deltasUserFunc = DeltasUserFunc()
def DeltasUser():#
    n = 0
    def func():#
        print('> DeltasUser ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def initUserStart(iduser):#
    deltasUser.set_n(iduser)
def initUserEnd(iduser):#
    return deltasUser.get_n()
deltasUser = DeltasUser()
def DeltasServer():#
    n = 0
    def func():#
        print('> DeltasServer ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def initServerStart(iduser):#
    deltasServer.set_n(iduser)
def initServerEnd(iduser):#
    return deltasServer.get_n()
deltasServer = DeltasServer()
#
def DeltasSchedules():#
    n = 0
    def func():#
        print('> DeltasSchedules ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def initSchedulesStart(iduser):#
    deltasSchedules.set_n(iduser)
def initSchedulesEnd(iduser):#
    return deltasSchedules.get_n()
deltasSchedules = DeltasSchedules()
#
def DeltasAssembly():#
    n = 0
    def func():#
        print('> DeltasAssembly ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def initAssemblyStart(iduser):#
    deltasAssembly.set_n(iduser)
def initAssemblyEnd(iduser):#
    return deltasAssembly.get_n()
deltasAssembly = DeltasAssembly()
#
def DeltasLogin():#
    n = 0
    def func():#
        print('> DeltasLogin ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def initloginStart(iduser):#
    deltasLogin.set_n(iduser)
def initloginEnd(iduser):#
    return deltasLogin.get_n()
deltasLogin = DeltasLogin()
#
def DeltasFunctions():#
    n = 0
    def func():#
        print('> DeltasFunctions ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def initFunctionsStart(iduser):#
    deltasFunctions.set_n(iduser)
def initFunctionsEnd(iduser):#
    return deltasFunctions.get_n()
deltasFunctions = DeltasFunctions()
#
def ViewPort():#
    n = 0
    def func():#
        print('> ViewPort ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def initViewPortsStart(iduser):#
    viewPorts.set_n(iduser)
def initViewPortsEnd(iduser):#
    return viewPorts.get_n()
viewPorts = ViewPort()
#
def Rig():#
    n = 0
    def func():#
        print('> Rig ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def initRigStart(iduser):#
    viewPorts.set_n(iduser)
def initRigEnd(iduser):#
    return viewPorts.get_n()
rig = Rig()
#
def Mouse():#
    n = 0
    def func():#
        print('> Mouse ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def initMouseStart(iduser):#
    mouse.set_n(iduser)
def initMouseEnd(iduser):#
    return mouse.get_n()
mouse = Mouse()
def Request():#
    n = 0
    def func():#
        print('> Request ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def initRequestStart(iduser):#
    request.set_n(iduser)
def initRequestEnd(iduser):#
    return request.get_n()
request = Request()
def ServerStart():#
    n = 0
    def func():#
        print('> ServerStart ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def initServerStart(iduser):#
    servstart.set_n(iduser)
def initServerEnd(iduser):#
    return servstart.get_n()
servstart = ServerStart()
