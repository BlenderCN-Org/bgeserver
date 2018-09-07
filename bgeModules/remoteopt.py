# !/usr/bin/env python .
# Created Monday, July 30, 2018 .
# Blender 2.79 remoteopt.py
# 
# Last update :
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
def enterRemoteOpOpt(remoteopt):#
    remoteOp.set_n(remoteopt)
def returnRemoteOpOpt(remoteopt):#
    return remoteOp.get_n()
def enterRemotePipOpt(remoteopt):#
    remotePip.set_n(remoteopt)
def returnRemotePipOpt(remoteopt):#
    return remotePip.get_n()
def enterRemoteWpOpt(remoteopt):#
    remotePos.set_n(remoteopt)
def returnRemoteWpOpt(remoteopt):#
    return remotePos.get_n()
def enterRemoteSatOpt(remoteopt):#
    remoteSat.set_n(remoteopt)
def returnRemoteSatOpt(remoteopt):#
    return remoteSat.get_n()
def enterRemoteFasOpt(remoteopt):#
    remoteFas.set_n(remoteopt)
def returnRemoteFasOpt(remoteopt):#
    return remoteFas.get_n()
def enterRemoteGlobOpt(remoteopt):#
    remoteGlob.set_n(remoteopt)
def returnRemoteGlobOpt(remoteopt):#
    return remoteGlob.get_n()
remoteOp = RemoteOp()
remotePip = RemotePip()
remotePos = RemotePos()
remoteFas = RemoteFas()
remoteSat = RemoteSat()
remoteGlob = RemoteGlob()
