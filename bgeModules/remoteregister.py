# !/usr/bin/env python .
# Created Friday, June 29, 2018 .
# Blender 2.79 remoteregister.py
# 
# Last update :
def Register():#
    n = 0
    def func():#
        print('> Register', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def closeRegister(remoteregister):#
    register.set_n(remoteregister)
def openRegister(remoteregister):#
    return register.get_n()
register = Register()
