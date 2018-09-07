# !/usr/bin/env python .
# Created Tuesday, June 26, 2018 .
# Blender 2.79 classclient.py
# 
# Last update :
def Singlepass():#
    n = 0
    def func():#
        print('> Singlepass', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def Multipass():#
    n = 0
    def func():#
        print('> Multipass', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def init_single(classclient):#
    singlepass.set_n(classclient)
def single(classclient) :#
    return singlepass.get_n()
def init_multi(classclient):#
    multipass.set_n(classclient)
def multi(classclient) :#
    return multipass.get_n()
singlepass = Singlepass()
multipass = Multipass()
    #    
    
