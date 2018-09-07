# !/usr/bin/env python .
# Created Wednesday, August 8, 2018 .
# Blender 2.79 consoleclass.py
# 
# Last update :
#
class Console:#_____________________________________________________________________________:(
    def __init__(self):#
        self.con = 0
    def count(self):#
        self.con  = togCon.get_n() + 1
        togCon.set_n(self.con)
    def discount(self):#
        out = togCon.get_n() - 1
        togCon.set_n(out)
#
class ConsoleBackSpace:#_____________________________________________________________________________:(
    def __init__(self):#   
        self.backSP = 0
    def count(self):#
        self.backSP  = togBackSpace.get_n() + 1
        togBackSpace.set_n(self.backSP)
        if togBackSpace.get_n() == 4:#
            togBackSpace.set_n(0)
            togLeftShiftkey.set_n(0)
            self.backSP = 0
#
class ConsoleESC:#_____________________________________________________________________________:(
    def __init__(self):#
        self.esc = 0
    def count(self):#
        self.esc  = togESCkey.get_n() + 1
        togESCkey.set_n(self.esc)
    def discount(self):#
        out = togESCkey.get_n() - 1
        togESCkey.set_n(out)
#
class ConsoleTab:#_____________________________________________________________________________:(
    def __init__(self):#
        self.tab = 0
    def count(self):#
        self.tab  = tabCon.get_n() + 1
        tabCon.set_n(self.tab)
        self.limit()
    def limit(self):#
        if tabCon.get_n() == 5:#
            tabCon.set_n(0)
class ConsoleTKey:#_____________________________________________________________________________:(
    def __init__(self):#
        self.T = 0
    def count(self):#
        self.T  = togTkey.get_n() + 1
        togTkey.set_n(self.T)
    def decount(self):#
        out = togTkey.get_n() - 1
        togTkey.set_n(out)
#
class ConsoleFunc:#_____________________________________________________________________________:(
    def __init__(self):#
        self.func = 0
    def count(self):#
        self.func  = funcCon.get_n() + 1
        funcCon.set_n(self.func)
    def discount(self):#
        out = funcCon.get_n() - 1
        funcCon.set_n(out)
#
class ConsoleRightShift:#_____________________________________________________________________________:(
    def __init__(self):#
        self.Rshift = 0
    def count(self):#
        self.Rshift  = togRightShiftkey.get_n() + 1
        togRightShiftkey.set_n(self.Rshift)
    def decount(self):#
        out = togRightShiftkey.get_n() - 1
        togRightShiftkey.set_n(out)
#
class ConsoleLeftShift:#_____________________________________________________________________________:(
    def __init__(self):#
        self.Lshift = 0
    def count(self):#
        self.Lshift  = togLeftShiftkey.get_n() + 1
        togLeftShiftkey.set_n(self.Lshift)
    def decount(self):#
        out = togLeftShiftkey.get_n() - 1
        togLeftShiftkey.set_n(out)
#
class ConsoleRightAlt:#_____________________________________________________________________________:(
    def __init__(self):#
        self.Ralt = 0
    def count(self):#
        self.Ralt  = togRightAltkey.get_n() + 1
        togRightAltkey.set_n(self.Ralt)
    def discount(self):#
        out = togRightAltkey.get_n() - 1
        togRightAltkey.set_n(out)
#
class ConsoleLeftAlt:#_____________________________________________________________________________:(
    def __init__(self):#
        self.Lalt = 0
    def count(self):#
        self.Lalt  = togLeftAltkey.get_n() + 1
        togLeftAltkey.set_n(self.Lalt)
    def discount(self):#
        out = togLeftAltkey.get_n() - 1
        togLeftAltkey.set_n(out)
#
class ConsoleRightCtrl:#_____________________________________________________________________________:(
    def __init__(self):#
        self.Rctrl = 0
    def count(self):#
        self.Rctrl  = togRightCtrlkey.get_n() + 1
        togRightCtrlkey.set_n(self.Rctrl)
    def discount(self):#
        out = togRightCtrlkey.get_n() - 1
        togRightCtrlkey.set_n(out)
#
class ConsoleLeftCtrl:#_____________________________________________________________________________:(
    def __init__(self):#
        self.Lctrl = 0
    def count(self):#
        self.Lctrl  = togLeftCtrlkey.get_n() + 1
        togLeftCtrlkey.set_n(self.Lctrl)
    def discount(self):#
        out = togLeftCtrlkey.get_n() - 1
        togLeftCtrlkey.set_n(out)
#
class ConsoleCapsLock:#_____________________________________________________________________________:(
    def __init__(self):#
        self.caps = 0
    def count(self):#
        self.caps  = togCapsLockkey.get_n() + 1
        togCapsLockkey.set_n(self.caps)
    def discount(self):#
        out = togCapsLockkey.get_n() - 1
        togCapsLockkey.set_n(out)
#
class ConsoleFuncF1:#_____________________________________________________________________________:(
    def __init__(self):#
        self.funcF1 = 0
    def count(self):#
        self.funcF1  = togF1key.get_n() + 1
        togF1key.set_n(self.funcF1)
    def discount(self):#
        out = togF1key.get_n() - 1
        togF1key.set_n(out)
#
class ConsoleFuncF2:#_____________________________________________________________________________:(
    def __init__(self):#
        self.funcF2 = 0
    def count(self):#
        self.funcF2  = togF2key.get_n() + 1
        togF2key.set_n(self.funcF2)
    def discount(self):#
        out = togF2key.get_n() - 1
        togF2key.set_n(out)
#
class ConsoleFuncF3:#_____________________________________________________________________________:(
    def __init__(self):#
        self.funcF3 = 0
    def count(self):#
        self.funcF3  = togF3key.get_n() + 1
        togF3key.set_n(self.funcF3)
    def discount(self):#
        out = togF3key.get_n() - 1
        togF3key.set_n(out)
#
class ConsoleFuncF4:#_____________________________________________________________________________:(
    def __init__(self):#
        self.funcF4 = 0
    def count(self):#
        self.funcF4  = togF4key.get_n() + 1
        togF4key.set_n(self.funcF4)
    def discount(self):#
        out = togF4key.get_n() - 1
        togF4key.set_n(out)
#
class ConsoleFuncF5:#_____________________________________________________________________________:(
    def __init__(self):#
        self.funcF5 = 0
    def count(self):#
        self.funcF5  = togF5key.get_n() + 1
        togF5key.set_n(self.funcF5)
    def discount(self):#
        out = togF5key.get_n() - 1
        togF5key.set_n(out)
#
class ConsoleFuncF6:#_____________________________________________________________________________:(
    def __init__(self):#
        self.funcF6 = 0
    def count(self):#
        self.funcF6  = togF6key.get_n() + 1
        togF6key.set_n(self.funcF6)
    def discount(self):#
        out = togF6key.get_n() - 1
        togF6key.set_n(out)
#
class ConsoleFuncF7:#_____________________________________________________________________________:(
    def __init__(self):#
        self.funcF7 = 0
    def count(self):#
        self.funcF7  = togF7key.get_n() + 1
        togF7key.set_n(self.funcF7)
    def discount(self):#
        out = togF7key.get_n() - 1
        togF7key.set_n(out)
#
class ConsoleFuncF8:#_____________________________________________________________________________:(
    def __init__(self):#
        self.funcF8 = 0
    def count(self):#
        self.funcF8  = togF8key.get_n() + 1
        togF8key.set_n(self.funcF8)
    def discount(self):#
        out = togF8key.get_n() - 1
        togF8key.set_n(out)
#
class ConsoleFuncF9:#_____________________________________________________________________________:(
    def __init__(self):#
        self.funcF9 = 0
    def count(self):#
        self.funcF9  = togF9key.get_n() + 1
        togF9key.set_n(self.funcF9)
    def discount(self):#
        out = togF9key.get_n() - 1
        togF9key.set_n(out)
#
class ConsoleFuncF10:#_____________________________________________________________________________:(
    def __init__(self):#
        self.funcF10 = 0
    def count(self):#
        self.funcF10  = togF10key.get_n() + 1
        togF10key.set_n(self.funcF10)
    def discount(self):#
        out = togF10key.get_n() - 1
        togF10key.set_n(out)
#
class ConsoleFuncF11:#_____________________________________________________________________________:(
    def __init__(self):#
        self.funcF11 = 0
    def count(self):#
        self.funcF11  = togF11key.get_n() + 1
        togF11key.set_n(self.funcF11)
    def decount(self):#
        out = togF11key.get_n() - 1
        togF11key.set_n(out)
#
class ConsoleFuncF12:#_____________________________________________________________________________:(
    def __init__(self):#
        self.funcF12 = 0
    def count(self):#
        self.funcF12  = togF12key.get_n() + 1
        togF12key.set_n(self.funcF12)
    def decount(self):#
        out = togF12key.get_n() - 1
        togF12key.set_n(out)
#######################################################
def TogTabkey():#
    n = 0
    def func():#
        print('> TogTabkey ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def TogCapsLockkey():#
    n = 0
    def func():#
        print('> TogCapsLockkey ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_______________
def TogLeftCtrlkey():#
    n = 0
    def func():#
        print('> TogLeftCtrlkey ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_______________
def TogRightCtrlkey():#
    n = 0
    def func():#
        print('> TogRightCtrlkey ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_______________
def TogLeftAltkey():#
    n = 0
    def func():#
        print('> TogLeftAltkey ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_______________
def TogRightAltkey():#
    n = 0
    def func():#
        print('> TogRightAltkey ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_______________
def TogLeftShiftkey():#
    n = 0
    def func():#
        print('> TogLeftShiftkey ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_______________#
def TogRightShiftkey():#
    n = 0
    def func():#
        print('> TogRightShiftkey ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#___________________________
#############################################################
def TogF1key():#
    n = 0
    def func():#
        print('> TogF1key ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def TogF2key():#
    n = 0
    def func():#
        print('> TogF2key ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def TogF3key():#
    n = 0
    def func():#
        print('> TogF3key ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def TogF4key():#
    n = 0
    def func():#
        print('> TogF4key ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def TogF5key():#
    n = 0
    def func():#
        print('> TogF5key ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def TogF6key():#
    n = 0
    def func():#
        print('> TogF6key ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def TogF7key():#
    n = 0
    def func():#
        print('> TogF7key ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def TogF8key():#
    n = 0
    def func():#
        print('> TogF8key ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def TogF9key():#
    n = 0
    def func():#
        print('> TogF9key ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def TogF10key():#
    n = 0
    def func():#
        print('> TogF10key ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def TogF11key():#
    n = 0
    def func():#
        print('> F11.key ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def TogF12key():#
    n = 0
    def func():#
        print('> F12.key ', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
###################################
togCon = TogCon()
togBackSpace = TogBackSpace()
togESCkey = TogESCkey()
togTabkey = TogTabkey()
## togEnterkey = TogEnterkey()  ? ? ?
togRightShiftkey = TogRightShiftkey()
togLeftShiftkey = TogLeftShiftkey()
togRightAltkey = TogRightAltkey() 
togLeftAltkey = TogLeftAltkey()  
togRightCtrlkey = TogRightCtrlkey() 
togLeftCtrlkey = TogLeftCtrlkey()
togCapsLockkey = TogCapsLockkey()
################################
console = Console()#
consoleBackSpace = ConsoleBackSpace()#
consoleESC = ConsoleESC()#
consoleTKey = ConsoleTKey()#
consoleTab = ConsoleTab()#
consoleFunc = ConsoleFunc()#
consoleRightShift = ConsoleRightShift()
consoleLeftShift = ConsoleLeftShift()
consoleRightAlt = ConsoleRightAlt()
consoleLeftAlt = ConsoleLeftAlt()
consoleRightCtrl = ConsoleRightCtrl()
consoleLeftCtrl = ConsoleLeftCtrl()
consoleCapsLock = ConsoleCapsLock()
##########################
togF1key = TogF1key()
togF2key = TogF2key()
togF3key = TogF3key()
togF4key = TogF4key()
togF5key = TogF5key()
togF6key = TogF6key()
togF7key = TogF7key()
togF8key = TogF8key()
togF9key = TogF9key()
togF10key = TogF10key()
togF11key = TogF11key()
togF12key = TogF12key()
#########################
consoleFuncF1 = ConsoleFuncF1()
consoleFuncF2 = ConsoleFuncF2()
consoleFuncF3 = ConsoleFuncF3()
consoleFuncF4 = ConsoleFuncF4()
consoleFuncF5 = ConsoleFuncF5()
consoleFuncF6 = ConsoleFuncF6()
consoleFuncF7 = ConsoleFuncF7()
consoleFuncF8 = ConsoleFuncF8()
consoleFuncF9 = ConsoleFuncF9()
consoleFuncF10 = ConsoleFuncF10()
consoleFuncF11 = ConsoleFuncF11()
consoleFuncF12 = ConsoleFuncF12()
