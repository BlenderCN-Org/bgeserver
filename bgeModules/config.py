# !/usr/bin/env python .
# Created Sunday, June 24, 2018 .
# Blender 2.79 config.py
# 
# Last update :
def ClientAddress():#
    n = 0
    def func():#
        print('> ClientAddress', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def ClientName():#
    n = 0
    def func():#
        print('> ClientName', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setAddress(config):#
    clientAddress.set_n(config)
def getAddress(config):#
    return clientAddress.get_n()
def setName(config):#
    clientName.set_n(config)
def getName(config):#
    return clientName.get_n()
clientAddress = ClientAddress()
clientName = ClientName()#
def ClientOpen():#
    n = 0
    def func():#
        print('> ClientOpen', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def ClientClose():#
    n = 0
    def func():#
        print('> ClientClose', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def RemoteOpen():#
    n = 0
    def func():#
        print('> RemoteOpen', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def RemoteClose():#
    n = 0
    def func():#
        print('> RemoteClose', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def closeClient(config):#
    clientOpen.set_n(config)
def openClient(config):#
    return clientOpen.get_n()
def closeRemote(config):#
    remoteClose.set_n(config)
def openRemote(config):#
    return remoteClose.get_n()
clientOpen = ClientOpen()
clientClose = ClientClose()
remoteOpen = RemoteOpen()
remoteClose = RemoteClose()
def Request():#
    n = 0
    def func():#
        print('> Request', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def closeRequest(config):#
    request.set_n(config)
def openRequest(config):#
    return request.get_n()
request = Request()
