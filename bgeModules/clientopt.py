# !/usr/bin/env python .
# Created Monday, July 30, 2018 .
# Blender 2.79 clientopt.py
# 
# Last update :
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
def enterClientOpOpt(clientopt):#
    clientOp.set_n(clientopt)
def returnClientOpOpt(clientopt):#
    return clientOp.get_n()
def enterClientPipOpt(clientopt):#
    clientPip.set_n(clientopt)
def returnClientPipOpt(clientopt):#
    return clientPip.get_n()
def enterClientWpOpt(clientopt):#
    clientPos.set_n(clientopt)
def returnClientWpOpt(clientopt):#
    return clientPos.get_n()
def enterClientSatOpt(clientopt):#
    clientSat.set_n(clientopt)
def returnClientSatOpt(clientopt):#
    return clientSat.get_n()
def enterClientFasOpt(clientopt):#
    clientFas.set_n(clientopt)
def returnClientFasOpt(clientopt):#
    return clientFas.get_n()
def enterClientGlobOpt(clientopt):#
    clientGlob.set_n(clientopt)
def returnClientGlobOpt(clientopt):#
    return clientGlob.get_n()
clientOp = ClientOp()
clientPip = ClientPip()
clientPos = ClientPos()
clientFas = ClientFas()
clientSat = ClientSat()
clientGlob = ClientGlob()
