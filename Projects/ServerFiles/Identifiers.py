#!/usr/bin/env python
#/ Last Backup / 2017 / Feb / 04 / Current Projects / ThreadingServer101.py
#/ Module /Identifiers.py
def ModuleLoader():#
    n = 0#
    def func():#
        print('> Module >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#mod001 = ModuleLoader)#
#mod001.set_n(1)#
#mod001()#___________
#
def TimeDate():#
    n = 0#
    def func():#
        print('> Time_Date >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#td= TimeDate()#
#td.set_n(1)#
#td()#___________
def Invalid():#
    n = 0#
    def func():#
        print('> Invalid >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#inv = Invalid()#
#inv.set_n(1)#
#inv()#___________
def EnterRec():#
    n = 0#
    def func():#
        print('> Enter_Menu >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#enter = EnterRec()#
#enter.set_n(1)#
#enter()#___________
def AddRec():#
    n = 0#
    def func():#
        print('> Add_Rec >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#addr = AddRec()#
#addr .set_n(1)#
#addr()#___________
def LookupRec():#
    n = 0#
    def func():#
        print('> Lookup_Rec >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#lur = LookupRec()#
#lur.set_n(1)#
#lur()#___________
def UploadRec():#
    n = 0#
    def func():#
        print('> Upload_Rec >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#ulr = UploadRec()#
#ulr.set_n(1)#
#ulr()#___________
def DownloadRec():#
    n = 0#
    def func():#
        print('> Download_Rec >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#dlr = DownloadRec()#
#dlr.set_n(1)#
#dlr()#___________
def ListRec():#
    n = 0#
    def func():#
        print('> List_Rec >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#ltr = ListRec()#
#ltr.set_n(1)#
#ltr()#___________
def ExitRec():#
    n = 0#
    def func():#
        print('> Exit_Menu >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#extr = 