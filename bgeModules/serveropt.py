# !/usr/bin/env python .
# Created Friday, June 29, 2018 .
# Blender 2.79 serveropt.py
# 
# Last update : 
def Opt():#
    n = 0
    def func():#
        print('> Opt', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def conOpt(serveropt):#
    return opt.get_n()
def disOpt(serveropt):#
    opt.set_n(serveropt)#
opt = Opt()
