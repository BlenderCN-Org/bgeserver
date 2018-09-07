# !/usr/bin/env python .
# Created Thursday, August 16, 2018 .
# Blender 2.79 configdeltas.py
# 
# Last update :
def Main():#
    n = 0
    def func():#
        print('> Main ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def deleteMain(configdeltas):#
    main.set_n(configdeltas)
def loadMain(configdeltas):#
    return main.get_n()
main = Main()
def Login():#
    n = 0
    def func():#
        print('> Login ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def deletelogin(configdeltas):#
    login.set_n(configdeltas)
def loadlogin(configdeltas):#
    return login.get_n()
login = Login()
#
def Server():#
    n = 0
    def func():#
        print('> Server ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def deleteserver(configdeltas):#
    server.set_n(configdeltas)
def loadserver(configdeltas):#
    return server.get_n()
server = Server()
#
def Schedules():#
    n = 0
    def func():#
        print('> Schedules ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def deleteschedules(configdeltas):#
    schedules.set_n(configdeltas)
def loadschedules(configdeltas):#
    return schedules.get_n()
schedules = Schedules()
#
def Assembly():#
    n = 0
    def func():#
        print('> Assembly ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def deleteassembly(configdeltas):#
    assembly.set_n(configdeltas)
def loadassembly(configdeltas):#
    return assembly.get_n()
assembly = Assembly()
#
def Functions():#
    n = 0
    def func():#
        print('> Functions ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def deletefunctions(configdeltas):#
    functions.set_n(configdeltas)
def loadfunctions(configdeltas):#
    return functions.get_n()
functions = Functions()
#
def Viewport():#
    n = 0
    def func():#
        print('> Viewport ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def deleteviewport(configdeltas):#
    viewport.set_n(configdeltas)
def loadviewport(configdeltas):#
    return viewport.get_n()
viewport = Viewport()
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
def deleteRig(configdeltas):#
    rig.set_n(configdeltas)
def loadRig(configdeltas):#
    return rig.get_n()
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
def deletemouse(configdeltas):#
    mouse.set_n(configdeltas)
def loadmouse(configdeltas):#
    return mouse.get_n()
mouse = Mouse()
def Change():#
    n = 0
    def func():#
        print('> Change ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def deletechange(configdeltas):#
    change.set_n(configdeltas)
def loadchange(configdeltas):#
    return change.get_n()
change = Change()
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
def deleterequest(configdeltas):#
    change.set_n(configdeltas)
def loadrequest(configdeltas):#
    return change.get_n()
request = Request()
