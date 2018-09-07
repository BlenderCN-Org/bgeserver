# !/usr/bin/env python .
# Created Friday, June 29, 2018 .
# Blender 2.79 serverconfig.py
# 
# Last update : 
def Config():#
    n = 0
    def func():#
        print('> Config', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def conConfig(serverconfig):#
    return config.get_n()
def disConfig(serverconfig):#
    config.set_n(serverconfig)#
config = Config()    
