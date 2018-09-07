# !/usr/bin/env python .
# Created Tuseday, July 31, 2018 .
# Blender 2.79 wpuser.py
# 
# Last update :
def UserWp():#
    n = 0
    def func():#
        print('> UserWp', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setClientWp(wpuser):#
    userWp.set_n(wpuser)
def getClientWp(wpuser):#
    return userWp.get_n()
userWp = UserWp()
