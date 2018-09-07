# !/usr/bin/env python .
# Created Monday, July 16, 2018 .
# Blender 2.79 clientconfig.py
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
def ClientOp():#
    n = 0
    def func():#
        print('> ClientOp ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def ClientPos():#
    n = 0
    def func():#
        print('> ClientPos ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def ClientPip():#
    n = 0
    def func():#
        print('> ClientPip ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def ClientSat():#
    n = 0
    def func():#
        print('> ClientSat ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def ClientFas():#
    n = 0
    def func():#
        print('> ClientFas ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def ClientGlob():#
    n = 0
    def func():#
        print('> ClientGlob ', n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def enterClientPip(clientconfig):#
    clientPip.set_n(clientconfig)
def returnClientPip(clientconfig):#
    return clientPip.get_n()
def enterClientOp(clientconfig):#
    clientOp.set_n(clientconfig)
def returnClientOp(clientconfig):#
    return clientOp.get_n()
def enterClientWp(clientconfig):#
    clientPos.set_n(clientconfig)
def returnClientWp(clientconfig):#
    return clientPos.get_n()
def enterClientSat(clientconfig):#
    clientSat.set_n(clientconfig)
def returnClientSat(clientconfig):#
    return clientSat.get_n()
def enterClientFas(clientconfig):#
    clientFas.set_n(clientconfig)
def returnClientFas(clientconfig):#
    return clientFas.get_n()
def enterClientGlob(clientconfig):#
    clientGlob.set_n(clientconfig)
def returnClientGlob(clientconfig):#
    return clientGlob.get_n()
clientOp = ClientOp()
clientPip = ClientPip()
clientPos = ClientPos()
clientFas = ClientFas()
clientSat = ClientSat()
clientGlob = ClientGlob()
