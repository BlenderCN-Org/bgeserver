# !/usr/bin/env python .
# Created Saturday, June 30, 2018 .
# Blender 2.79 movieflics.py 
# 
# Last update :
def Movies():#
    n = 0
    def func():#
        print('> Movies', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def onMovie(movieflics):#
    return movies.get_n()
def offMovie(movieflics):#
    movies.set_n(movieflics)
movies = Movies()    
