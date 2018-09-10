#!/usr/bin/env python
#/ Last Backup / 2017 / Feb / 12 / Current Projects / ThreadingServer101.py
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
#extr = ExitRec()#
#extr.set_n(1)#
#extr()#___________
def DirList():#
    n = 0#
    def func():#
        print('> Dir_List >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#md = DirList()#
#md.set_n(1)#
#md()#___________
def DirChange():#
    n = 0#
    def func():#
        print('> Dir_Change >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#dc = DirChange()#
#dc.set_n(1)#
#dc()#___________
def MakeDirectory():#
    n = 0#
    def func():#
        print('> Make_Dir >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#mdy = MakeDirectory()#
#mdy.set_n(1)#
#mdy()#___________
#
def SystemLocks():#
    n = 0#
    def func():#
        print('> System_Locks >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#syslk = SystemLocks()#
#syslk.set_n(1)#
#syslk()#___________
#_________________
def AddRecLock():#
    n = 0#
    def func():#
        print('> AddRec_Lock >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#adrk = AddRecLock()#
#adrk.set_n(1)#
#adrk()#___________
#
def Pics_Codec():#
    n = 0#
    def func():#
        print('> Codec Load >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#pcd = Pics_Codec()#
#pcd.set_n(1)#
#pcd()#___________
##def DuplicatedFile():#
##    n = 0#
##    def func():#
##        print('> Duplicated File >', n)# 
##    def get_n():#
##        return n#
##    def set_n(value):#
##        nonlocal n#
##        n = value#
##    func.get_n = get_n#
##    func.set_n = set_n#
##    return func#
#dup = DuplicatedFile()#
#dup.set_n(1)#
#dup()#
##def DickeyStore():#
##    n = 0#
##    def func():#
##        print('> Dic_Key_Store > ', n)# 
##    def get_n():#
##        return n#
##    def set_n(value):#
##        nonlocal n#
##        n = value#
##    func.get_n = get_n#
##    func.set_n = set_n#
##    return func#
#dkys = DickeyStore()#
#dkys.set_n(1)#
#dkys()#
##def ServiceDirectories():#
##    n = 0#
##    def func():#
##        print('> Current path > ', n)# 
##    def get_n():#
##        return n#
##    def set_n(value):#
##        nonlocal n#
##        n = value#
##    func.get_n = get_n#
##    func.set_n = set_n#
##    return func#
#sdy = ServiceDirectories()#
#sdyset_n(1)#
#sdy()#
##def LoadCurrentDirectory():#
##    n = 0#
##    def func():#
##        print('> Load Cur Dir', n)# 
##    def get_n():#
##        return n#
##    def set_n(value):#
##        nonlocal n#
##        n = value#
##    func.get_n = get_n#
##    func.set_n = set_n#
##    return func#
#lcd = LoadCurrentDirectory()#
#lcd.set_n(1)#
#lcd()#
##def NewKey():#
##    n = 0#
##    def func():#
##        print('> Directory Service ', n)# 
##    def get_n():#
##        return n#
##    def set_n(value):#
##        nonlocal n#
##        n = value#
##    func.get_n = get_n#
##    func.set_n = set_n#
##    return func#
#nk = NewKey()#
#nk.set_n(1)#
#nk()#
##def FileSizer():#
##    n = 0#
##    def func():#
##        print('> Socket Size >', n)# 
##    def get_n():#
##        return n#
##    def set_n(value):#
##        nonlocal n#
##        n = value#
##    func.get_n = get_n#
##    func.set_n = set_n#
##    return func#
#fs = FileSizer()#
#fs.set_n(1)#
#fs()#
##def StoreRequestkey():#
##    n = 0#_____
##    def func():#__________________
##        print('> Request key', n)# 
##    def get_n():#
##        return n#____
##    def set_n(value):#
##        nonlocal n#
##        n = value#_____
##    func.get_n = get_n#
##    func.set_n = set_n#
##    return func#
##dk = StoreRequestkey()
##dk.get_n()
##dk.set_n(dic)
##dk()
##def DireectoryList():#
##    n = 0#
##    def func():#
##        print('> Direectory List :', n)# 
##    def get_n():#
##        return n#
##    def set_n(value):#
##        nonlocal n#
##        n = value#
##    func.get_n = get_n#
##    func.set_n = set_n#
##    return func#
#dylls= DireectoryList()#
#dylls.set_n(1)#
#dylls()#
