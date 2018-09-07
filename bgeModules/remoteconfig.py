# !/usr/bin/env python .
# Created Monday, July 16, 2018 .
# Blender 2.79 remoteconfig.py
# 
# Last update :
''' Place Holder Tank for Main Functions . '''
''' Old Functions before modules . '''
''' spawnRemote : gladHands : msgBreak : adminCenter : remoteCoordinates : remoteRevceive'''
''' The Heart for Remote Avatar . '''
''' command shell type : op : pip : multi1 : multi2 : ctrl : wp : sat : fas : glob . '''
''' > Short Forms . <'''
''' ["op"] = operator : Server returns other players name label . '''
''' ["pip"] = message break for server hand.Shake, verifies return address is correct or not . '''
#''' ["multi1, multi2"] = set player one & two Viewport and Keyboard Character controls .'''
#''' ["ctrl"] = control : User Command functions for players choice .'''
''' ["wp"] : set world position in Scene .'''
''' ["sat"] = satillites : get objects from server, Image Factory, Polygon Factory '''
''' ["fas"] = checks for satillite servers online or not .'''
''' ["glob"] = global position in world, sends User coordinates to Server .'''
''' command shell type : bypass : pass1 : rig1 < " for single User ! '''
def RemoteOp():#
    n = 0
    def func():#
        print('> RemoteOp ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def RemotePip():#
    n = 0
    def func():#
        print('> RemotePip ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def RemotePos():#
    n = 0
    def func():#
        print('> RemotePos ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def RemoteSat():#
    n = 0
    def func():#
        print('> RemoteSat ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def RemoteFas():#
    n = 0
    def func():#
        print('> RemoteFas ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def RemoteGlob():#
    n = 0
    def func():#
        print('> RemoteGlob ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def RemoteLog():#
    n = 0
    def func():#
        print('> RemoteLog ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def enterRemoteOp(remoteconfig):#
    remoteOp.set_n(remoteconfig)
def returnRemoteOp(remoteconfig):#
    return remoteOp.get_n()
def enterRemotePip(remoteconfig):#
    remotePip.set_n(remoteconfig)
def returnRemotePip(remoteconfig):#
    return remotePip.get_n()
def enterRemoteWp(remoteconfig):#
    remotePos.set_n(remoteconfig)
def returnRemoteWp(remoteconfig):#
    return remotePos.get_n()
def enterRemoteSat(remoteconfig):#
    remoteSat.set_n(remoteconfig)
def returnRemoteSat(remoteconfig):#
    return remoteSat.get_n()
def enterRemoteFas(remoteconfig):#
    remoteFas.set_n(remoteconfig)
def returnRemoteFas(remoteconfig):#
    return remoteFas.get_n()
def enterRemoteGlob(remoteconfig):#
    remoteGlob.set_n(remoteconfig)
def returnRemoteGlob(remoteconfig):#
    return remoteGlob.get_n()
def enterRemoteLog(remoteconfig):#
    remoteLog.set_n(remoteconfig)
def returnRemoteLog(remoteconfig):#
    return remoteLog.get_n()

remoteOp = RemoteOp()
remotePip = RemotePip()
remotePos = RemotePos()
remoteSat = RemoteSat()
remoteFas = RemoteFas()
remoteGlob = RemoteGlob()
remoteLog = RemoteLog()

