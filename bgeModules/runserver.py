# !/usr/bin/env python .
# Created Friday, June 29, 2018 .
# Blender 2.79 runserver.py
# 
# Last update :
def Server():#
    n = 0
    def func():#
        print('> Server ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def stop(runserver):#
    return server.get_n()
def start(runserver):#
    server.set_n(runserver)
server = Server()
