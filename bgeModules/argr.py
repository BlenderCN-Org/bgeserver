# !/usr/bin/env python .
# Created Friday, June 15, 2018 .
# Blender 2.79 argr.py
# 
# Last update : Sunday, July 29
def AgreeOp():#
    n = 0
    def func():#
        print('> AgreeOp ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def AgreePos():#
    n = 0
    def func():#
        print('> AgreePos ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def AgreePip():#
    n = 0
    def func():#
        print('> AgreePip ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def AgreeSat():#
    n = 0
    def func():#
        print('> AgreeSat ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def AgreeFas():#
    n = 0
    def func():#
        print('> AgreeFas ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def AgreeGlob():#
    n = 0
    def func():#
        print('> AgreeGlob ', n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def enterArgrPip(argr):#
    agreePip.set_n(argr)
def returnArgrPip(argr):#
    return agreePip.get_n()
def enterArgrOp(argr):#
    agreeOp.set_n(argr)
def returnArgrOp(argr):#
    return agreeOp.get_n()
def enterArgrWp(argr):#
    agreePos.set_n(argr)
def returnArgrWp(argr):#
    return agreePos.get_n()
def enterArgrSat(argr):#
    agreeSat.set_n(argr)
def returnArgrSat(argr):#
    return agreeSat.get_n()
def enterArgrFas(argr):#
    agreeFas.set_n(argr)
def returnArgrFas(argr):#
    return agreeFas.get_n()
def enterArgrGlob(argr):#
    agreeGlob.set_n(argr)
def returnArgrGlob(argr):#
    return agreeGlob.get_n()
agreeOp = AgreeOp()
agreePip = AgreePip()
agreePos = AgreePos()
agreeFas = AgreeFas()
agreeSat = AgreeSat()
agreeGlob = AgreeGlob()
