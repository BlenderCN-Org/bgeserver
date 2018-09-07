# !/usr/bin/env python .
# Created Thursday, June 28, 2018 .
# Blender 2.79 remoteuser.py
# 
# Last update : T
''' The Heart for Remote Avatar . '''
''' command shell type : op : pip : multi1 : multi2 : ctrl : wp : sat : fas : glob . '''
''' > Short Forms . <'''
''' ["op"] = operator : Starts the User spawn . '''
''' ["pip"] = message break for server hand.Shake, verifies return address is correct or not . '''
''' ["multi1, multi2"] = set player one & two Viewport and Keyboard Character controls .'''
''' ["ctrl"] = control : User Command functions for players choice .'''
''' ["wp"] : set world position in Scene .'''
''' ["sat"] = satillites : get objects from server, Image Factory, Polygon Factory '''
''' ["fas"] = checks for satillite servers online or not .'''
''' ["glob"] = global position in world, sends User coordinates to Server .'''
''' command shell type : bypass : pass1 : rig1 < " for single User ! '''
def Remote():#
    n = 0
    def func():#
        print('> Remote', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def Operator():#
    n = 0
    def func():#
        print('> Operator', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def Pipe():#
    n = 0
    def func():#
        print('>Pipe ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def closeRemote(remoteuser):#
    remote.set_n(remoteuser)
def openRemote(remoteuser):#
    return remote.get_n()
def closeOperator(remoteuser):#
    operator.set_n(remoteuser)
def openOperator(remoteuser):#
    return operator.get_n()
def closePipe(remoteuser):#
    pipe.set_n(remoteuser)
def openPipe(remoteuser):#
    return pipe.get_n()
remote = Remote()#
operator = Operator()
pipe = Pipe()
