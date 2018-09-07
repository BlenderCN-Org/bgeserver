# !/usr/bin/env python 3.4.1
# Threading Server for Blender Game Engine . 
# Created Friday, March 16, 2018 .
# Multi_user or Single_user  .
# Last updates : Saturday,  May 5,  2018 . (" startup.Procedures and client.Shutdown ")
import socket
import threading 
ipser = (socket.gethostbyname(socket.gethostname()))
print ('>>> bge * satellite servers . <<< ')
def DecodeServer(de):#__________________
    code = de.encode('ascii', 'ignore')#
    de = base64.b64decode(code)#
    return de#
def EncodeServer(en):#__________________
    code = en.encode('ascii', 'ignore')#
    en = base64.b64encode(code)#
    return en#
def byteraddr(raddr):#__________________:(
    return str(raddr).replace('" ','').replace('" ','')
def addcomma(mkco):#______:(
    return str(mkco).replace('[]',', ')
def whitespace(wspace):#______:(
    return str(wspace).replace('[]',' ')
def brackets(bkts):#_____________________:(
    return str(bkts).replace("[",'>').replace("]",'<')
def bracketremove1(bkts):#___________:(
    return str(bkts).replace('"','').replace('"','')
def bracketremove2(bkts):#__________:(
    return str(bkts).replace(' "','').replace(' "','')
def binit(inbin):#______:(
    return str(inbin).replace(' ','b" ').replace(' ',' " ')
def opt1_Indexing(adex):#_____________:(
    return str(adex).replace(' ',',')
def opt2_Indexing(bdex):#_____________:(
    return str(bdex).replace(' ',',')
def Floatcount():#_________________________________________________________________________:(
    n = 0
    def func():#
        print('>>> ',n ,' users alive in register .  <<<') 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Admin():#_____________________________________________________________________________:(
    n = 0
    def func():#
        print('> Admin ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Admin1Spawn():#______________________________________________________________________:(
    n = 0
    def func():#
        print('> Admin1Spawn ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Admin2Spawn():#______________________________________________________________________:(
    n = 0
    def func():#
        print('> Admin2Spawn ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Terminallock1():#______________________________________________________________________:(
    n = 0
    def func():#
        print('> Terminallock1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Player1():#___________________________________________________________________________:(
    n = 0
    def func():#
        print('> Player1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Player2():#___________________________________________________________________________:(
    n = 0
    def func():#
        print('> Player2 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Joinplayer_a1():#______________________________________________________________________:(
    n = 0
    def func():#
        print('> Joinplayer_a1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Joinplayer_a2():#______________________________________________________________________:(
    n = 0
    def func():#
        print('> Joinplayer_a2 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def SpawnPlayer_a3():#____________________________________________________________________:(
    n = 0
    def func():#
        print('> SpawnPlayer_a3 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def SpawnPlayer_b3():#____________________________________________________________________:(
    n = 0
    def func():#
        print('> SpawnPlayer_b3 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Joinplayer_b1():#______________________________________________________________________:(
    n = 0
    def func():#
        print('> Joinplayer_b1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Joinplayer_b2():#______________________________________________________________________:(
    n = 0
    def func():#
        print('> Joinplayer_b2 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def UsersRegister():#______________________________________________________________________:(
    n = 0
    def func():#
        print('> UsersRegister ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Bindport1():#__________________________________________________________________________:(
    n = 1
    def func():#
        print('> Bindport1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Bindport2():#__________________________________________________________________________:(
    n = 0
    def func():#__________________
        print('> Bindport2 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Binduser1():#__________________________________________________________________________:(
    n = 0
    def func():#
        print('> Binduser1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Binduser2():#__________________________________________________________________________:(
    n = 0
    def func():#
        print('> Binduser2 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def NameUpdater():#_______________________________________________________________________:(
    n = 0
    def func():#
        print('> NameUpdater ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Float1stp():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Float1stp ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Float2stp():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Float2stp ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def FloatPlayer1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> FloatPlayer1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def FloatPlayer2():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> FloatPlayer2', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Player1Name():#_______________________________________________________________________:(
    n = 0
    def func():#
        print('> Player1Name ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Player2Name():#_______________________________________________________________________:(
    n = 0
    def func():#
        print('> Player2Name ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Rec_a1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Rec_a1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Snd_a1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Snd_a1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Rec_b1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Rec_a1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Snd_b1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Snd_a1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Flashname_a1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Flashname_a1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Flashname_b1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Flashname_b1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Refresh():#___________________________________________________________________________:(
    n = 0
    def func():#
        print('> Refresh ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Refresh0ut():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Refresh0ut ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Refresh0ff():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Refresh0ff ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Refresh0n():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Refresh0n ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Spawners1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Spawners1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Spawners2():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Spawners2 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Spawn_a1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Spawn_a1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Spawn_b1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Spawn_b1 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Snda1msg():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Snda1msg ', n)
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Sndb1msg():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Sndb1msg ', n)
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Begin1Spawn():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Begin1Spawn ', n)
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Begin2Spawn():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Begin2Spawn ', n)
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Optsnd1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Optsnd1 ', n)
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Optsnd2():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Optsnd2 ', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Recv1Avatar():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Recv1Avatar ', n)   
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Recv2Avatar():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Recv2Avatar ', n)   
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Empty():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Empty', n)   
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Tmp():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Tmp', n)   
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Temp():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Temp', n)   
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Loops1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Loops1', n)   
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Loops2():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Loops2', n)   
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def  Loops3():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Loops3', n) 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Avatar1user():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Avatar1', n)  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Avatar2user():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Avatar2', n)  
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Ch1nl():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Ch1nl ', n)   
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Ch2nl():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Ch2nl ', n)  
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Ch3nl():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Ch3nl ', n)     
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Sig1nl():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Sig1nl ', n)    
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Sig2nl():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Sig2nl ', n) 
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Sig3nl():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Sig3nl ', n)      
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Cont1Opt():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Cont1Opt ', n)  
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Cont2Opt():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Cont2Opt ', n)  
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Main_a1snd():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Main_a1snd ', n) 
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Main_a2snd():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Main_a2snd ', n) 
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Main_b1snd():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Main_b1snd ', n) 
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Main_b2snd():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Main_b2snd ', n) 
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Break1Loop():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Break1Loop ', n) 
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Break2Loop():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Break2Loop ', n) 
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Vec1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Vec1 ', n) 
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Vec2():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Vec2 ', n) 
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   JoinVec1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  JoinVec1 ', n) 
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   JoinVec2():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  JoinVec2 ', n) 
        return n
    def get_n():#
        return n
    def set_n(value):
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   CtrlVec1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  CtrlVec1 ', n) 
        return n
    def get_n():
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   CtrlVec2():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  CtrlVec2 ', n) #
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Ctrl1Opt():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Ctrl1Opt ', n) #
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Ctrl2Opt():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Ctrl2Opt ', n) #
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Vec1Wp():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Vec1Wp  ', n) #
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Vec2Wp():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Vec2Wp  ', n) #
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Empty1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Empty1  ', n) #
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Empty2():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Empty1  ', n) #
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Cont1Opt():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Cont1Opt  ', n) #
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Cont2Opt():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Cont2Opt  ', n) #
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Position1User():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Position1User ', n) #
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Position2User():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Position2User ', n) #
        return n
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Center1Grid():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Center1Grid', n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Center2Grid():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Center2Grid' ,  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Multi1Player():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Multi1Player ',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Multi2Player():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Multi2Player ',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Close1User():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Close1User ',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Close2User():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Close2User',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Signal1Off():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Signal1Off',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Signal2Off():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Signal2Off',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Close1Opt():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Close1Opt',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Close2Opt():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Close2Opt',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Quit1():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Quit1',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   Quit2():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  Quit2',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   SelfRemote():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  SelfRemote',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def   SelfUser():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>  SelfUser',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def SelfBy1Pass():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> SelfBy1Pass',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def SelfBy2Pass():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> SelfBy2Pass',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def CmdPass():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> CmdPass',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Cmd1Pass():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Cmd1Pass',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Cmd2Pass():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Cmd2Pass',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Cmd3Pass():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Cmd3Pass',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Cmd4Pass():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Cmd4Pass',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Cmd5Pass():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Cmd5Pass',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Cmd6Pass():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Cmd6Pass',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Cmd7Pass():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Cmd7Pass',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def End1Remote():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> End1Remote',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def End2Remote():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> End2Remote',  n) #Cmd1Run
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Cmd1Run():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Cmd1Run',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Cmd1Post():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Cmd1Post',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Cmd2Post():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Cmd2Post',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Id1User():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Id1User',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Id2User():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> Id2User',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def IdSelf1User():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> IdSelf1User',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def IdSelf2User():#________________________________________________________________________:(
    n = 0
    def func():#
        print('> IdSelf2User',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def ShuntCount():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>>> remote shut down ',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Sub1Remote():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>>> Sub1Remote ',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Sub2Remote():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>>> Sub2Remote ',  n) #re1Global
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def re1Global():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>>> re1Global ',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def re2Global():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>>> re2Global ',  n) #
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def RigChange():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>>> RigChange ',  n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Arena1Opt():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>>> Arena1Opt',  n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Boundry1Opt():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>>> Boundry1Opt',  n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Arena2Opt():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>>> Arena2Opt',  n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Boundry2Opt():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>>> Boundry2Opt',  n) #  Sig1Pass
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
def Sig1Pass():#________________________________________________________________________:(
    n = 0
    def func():#
        print('>>> Sig1Pass',  n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
class Server:#____________________________________________________________________________:(socket.AF_INET, socket.SOCK_STREAM
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self):#
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind((ipser, 12345))
        self.serv.listen(0)
        self.updateraddr = []
        self.admin_raddr = []
        self.player1_raddr = []
        self.player2_raddr = []
        self.player_names = []
        self.config_users = []
        self.user1player = []
        self.user2player =[]
        self.User1Conn = []
        self.User2Conn = []
    def front_door(self, data, conn):#___________________________________________________________:(
        ''' Admins Front Door! ! '''
        main = str(threading.main_thread())
        active = str(threading.active_count())
        event = str(threading.Event())
        recvdata = data.decode("utf-8")
        def admin_set_register():#______________:(
            print(">>>_*admin_set register !  > ")
        def adminReset_spawn():#_______________:(
            print(">>>_*admin_reset_spawn !  > ")
        def adminSet_spawn():#__________________:(
            print(">>>_*admin_set_spawn !  > ")
        def admin1Send_labal():#________________:(
            print(">>>_*admin_set_user1 !  > ")
        def admin2Send_labal():#________________:(
            print(">>>_*admin_set_user2 !  > ")
        def admin1flashuser1():#______________________________:(
            print(">>>_*admin_set_world.Position_user1 !  > ")
        def admin1flashuser2():#______________________________:(
            print(">>>_*admin_set_world.Position_user2 ! > ")
        if  recvdata == 'reset':#> >. > .> .> .>. > .>. >. >.|.< .< .< .< .< .<. < .< .< .< 
            snd_data = ' config_reset '
            data = str.encode(snd_data, 'utf-8')
            joinplayer_a2.set_n(0)#
            joinplayer_b2.set_n(0)
            joinplayer_a1.set_n(0)
            joinplayer_b1.set_n(0) 
            adminreset = threading.Timer(1.0, adminReset_spawn)
            adminreset.start()
            #return data
        elif  recvdata == 'user':#
                snd_data = ' config_register . '
                data = str.encode(snd_data, 'utf-8')
                usersRegister.set_n(1)
                adminuser = threading.Timer(1.0, admin_set_register)
                adminuser.start()
                #return data
        #if sig1Pass.get_n() == 1:#
        elif  recvdata == 'det1':#
            snd_data = ' config_det1 . '
            data = str.encode(snd_data, 'utf-8')# 
            arena1Opt.set_n(1)
            arena2Opt.set_n(1)
        elif  recvdata == 'det2':#
            snd_data = ' config_det2 . '
            data = str.encode(snd_data, 'utf-8')
            boundry1Opt.set_n(1)
            boundry2Opt.set_n(1)
        elif  recvdata == 'rig1':#
            snd_data = ' config_rig1 . '
            data = str.encode(snd_data, 'utf-8')
            rigChange.set_n(1)
        elif  recvdata == 'cmdrun':#
            snd_data = ' config_cmdrun . '
            data = str.encode(snd_data, 'utf-8')
            cmdRun.set_n(1)
        elif  recvdata == 'pass1':#
            snd_data = ' config_cmd1pass . '
            data = str.encode(snd_data, 'utf-8')
            cmd1pass.set_n(1)
        elif  recvdata == 'pass2':#
            snd_data = ' config_cmd2pass . '
            data = str.encode(snd_data, 'utf-8')
            cmd2pass.set_n(1)
        elif  recvdata == 'bypass':#
            snd_data = ' config_bypass . '
            data = str.encode(snd_data, 'utf-8')
            selfby1pass.set_n(1)
            selfby2pass.set_n(1)
        elif  recvdata == 'multi1':#
            snd_data = ' config_multi player . '
            data = str.encode(snd_data, 'utf-8')
            multi1Player.set_n(1)
        elif  recvdata == 'multi2':#
            snd_data = ' config_multi player . '
            data = str.encode(snd_data, 'utf-8')
            multi2Player.set_n(1)
        elif  recvdata == 'pack':#
            snd_data = ' config_pack.junk . '
            data = str.encode(snd_data, 'utf-8')
            empty1.set_n(1) 
            empty2.set_n(1) 
        elif  recvdata == 'sat':#
            snd_data = ' config_satcom . '
            data = str.encode(snd_data, 'utf-8')
            position1User.set_n(1)
            position2User.set_n(1)
        elif  recvdata == 'glob':#
            snd_data = ' config_globals . '
            data = str.encode(snd_data, 'utf-8')
            joinplayer_a2.set_n(1)
            joinplayer_b2.set_n(1)
        elif  recvdata == 'pip':#
            snd_data = ' config_pipp1 . '
            data = str.encode(snd_data, 'utf-8')
            break1loop.set_n(1)
            break2loop.set_n(1)
        elif  recvdata == 'center':#
            snd_data = ' config_center_grid. '
            data = str.encode(snd_data, 'utf-8')
            center1Grid.set_n(1)
            center2Grid.set_n(1)
        elif  recvdata == 'vec':#
            snd_data = ' config_vec1. '
            data = str.encode(snd_data, 'utf-8')
            vec1.set_n(1)
            vec2.set_n(1)
        elif  recvdata == 'ctrl':#
            snd_data = ' config_ctrl1 . '
            data = str.encode(snd_data, 'utf-8')
            ctrl1Opt.set_n(1)
            ctrl2Opt.set_n(1)
        elif  recvdata == 'wp':#
            snd_data = ' config_wp . '
            data = str.encode(snd_data, 'utf-8')
            vec1wp.set_n(1)
            vec2wp.set_n(1)
        elif  recvdata == 'reset sig':#
            snd_data = ' config_reset sig  .'
            data = str.encode(snd_data, 'utf-8')
            sig1nl.set_n(0)
            sig2nl.set_n(0)
            sig3nl.set_n(0)
        elif  recvdata == 'op':#
            snd_data = ' config_register _op  . '
            data = str.encode(snd_data, 'utf-8')
            flashname_a1.set_n(1)#<<<<<<<___:(
            flashname_b1.set_n(1)#<<<<<<<___:(
        elif  recvdata == 'op1':#
            snd_data = ' config_register _op1  . '
            data = str.encode(snd_data, 'utf-8')
            flashname_a1.set_n(1)#<<<<<<<___:(
        elif  recvdata == 'op2':#
            snd_data = ' config_register _op2  .'
            data = str.encode(snd_data, 'utf-8')
            flashname_b1.set_n(1)#<<<<<<<___:(
        elif  recvdata == 'fas':#
            snd_data = ' config_flash . '
            data = str.encode(snd_data, 'utf-8')#
            cont1Opt.set_n(1)
            cont2Opt.set_n(1)
        elif  recvdata == 'empty1':#
            snd_data = ' config_empty 1  .'
            data = str.encode(snd_data, 'utf-8')#
        elif  recvdata == 'empty2':#
            snd_data = ' config_empty 2  .'
            data = str.encode(snd_data, 'utf-8')
        elif recvdata == 'clr':#
            snd_data = ' config_user names deleted  . '
            data = str.encode(snd_data, 'utf-8')   
            self.config_users = []
        elif  recvdata == 'names':#
            clr_brackets = brackets(self.config_users)
            snd_data = (' config_player names  . ' + clr_brackets)
            data = str.encode(snd_data, 'utf-8')
        elif recvdata == 'main':#
            data = str.encode(main, 'utf-8')   
        elif recvdata == 'active':#
            data = str.encode(active, 'utf-8')   
        elif recvdata == 'event':#
            data = str.encode(event, 'utf-8')   
        return data
    def admin_handler(self, conn, addr):#_______________________________________________________:(
        leave, raddr = addr
        try:#
            thread3Loop.loop3()
            while True:#
                ''' Insert comma ( commas )'''
                ''' Insert client address  ( servraddr )'''
                ''' Insert whitespace ( pkspace )'''
                mkco = []
                wspace = []
                data = conn.recv(1024)
                rtn_data = self.front_door(data, conn)
                pinint = byteraddr(raddr) 
                pkco = addcomma(mkco)
                pkspace = whitespace(wspace)
                servraddr = str.encode(pinint, 'utf-8')
                commas = str.encode(pkco, 'utf-8')        
                whspace = str.encode(pkspace, 'utf-8')
                conn.send(bytes(rtn_data+commas+servraddr))                    
                if not data:#
                    conn.close()
                    break
        except socket.error: #
            print('<<< admin_disconnection ! >>> ')#
            conn.close()
            adminUser.set_n(0)
    def player1_handler(self, conn, addr):#_____________________________________:(
        self.User1Conn = conn
        leave, raddr = addr
        self.player1_raddr = raddr #+|+
        mkco = []
        wspace = []
        bountryRig = '(:)'
        snd_rigBoundry  = str.encode(bountryRig, 'utf-8')
        arenaRig = '(.+.)'
        snd_rigArena = str.encode(arenaRig, 'utf-8')
        rig1Chg = '(|)'
        snd_rig1Chg  = str.encode(rig1Chg, 'utf-8')
        multi = 'multi1'
        pack_multi  = str.encode(multi, 'utf-8')
        remote2user = 'endObject'
        end_remote = str.encode(remote2user, 'utf-8')
        single1_pass = '<+>'
        single1User  = str.encode(single1_pass, 'utf-8')
        bypass = '<.|'
        snd_bypass  = str.encode(bypass, 'utf-8')
        close1 = '>|<'
        snd_close1  = str.encode(close1, 'utf-8')
        client1addr = str(raddr)
        sign1Off = ('clientgoodbye'+client1addr)
        food1 = 'packfood'
        pack_food1  = str.encode(food1, 'utf-8')
        grid1 = '+|+'
        center_grid1  = str.encode(grid1, 'utf-8')
        sat1 = 'sat1'
        worldPosistion = str.encode(sat1, 'utf-8')
        opt3 = 'vec_wp'
        ctrl3Opt_user1 = str.encode(opt3, 'utf-8')
        opt1 = 'ctrl'
        ctrl1Opt_user1 = str.encode(opt1, 'utf-8')
        vector1 = '-|-'
        vector_user1 = str.encode(vector1, 'utf-8')
        pipe_break1 = '|'
        pipe1 = str.encode(pipe_break1, 'utf-8')
        raddr_opt1 = str(raddr)
        remote1_raddr = str.encode(raddr_opt1, 'utf-8')
        serv1 = 'global_vectors'
        user_service1  = str.encode(serv1, 'utf-8')
        flash1 = str.encode(self.user1player, 'utf-8')
        pinint = byteraddr(raddr) 
        servraddr = str.encode(pinint, 'utf-8')
        pkco = addcomma(mkco)
        commas = str.encode(pkco, 'utf-8')    
        pkspace = whitespace(wspace)
        whspace = str.encode(pkspace, 'utf-8') 
        def spawner1():#
            print(">>> user1.Register * has_started_self.thread !  .*< ")
        spawned1 = threading.Timer(1.0, spawner1)
        spawned1.start()   
        try:#
            thread1Loop.loop1()
            while True:#
                main_a1snd.set_n(1) 
                def admin_break1():#
                    if break1loop.get_n() == 1:#
                        break1loop.set_n(0)
                        main_a1snd.set_n(0)
                        main_a2snd.set_n(1) 
                admin_break1()
                def admin_vec1():#
                    if vec1.get_n() == 1:#
                        vec1.set_n(0)
                        joinVec1.set_n(1)
                admin_vec1()
                data = conn.recv(1024)
                recvdata = data.decode("utf-8")
                def client1goodbye():#
                    def end1Object():#___________________________________________________________________:(
                        def end1Vals():#
                            close1User.set_n(0)
                            main_a1snd.set_n(0)
                            close1Opt.set_n(1)
                            signal1Off.set_n(1)
                            re1Global.set_n(0)
                            joinplayer_a2.set_n(0)
                            joinplayer_b2.set_n(0)
                            joinplayer_a1.set_n(0)
                            joinplayer_b1.set_n(0)
                        if close1User.get_n() == 1:#
                            if recvdata == sign1Off:#
                                if sub1Remote.get_n() == 0:#
                                    end1Vals()
                                    if end1Remote.get_n() == 1:#
                                        self.User2Conn.send(bytes(end_remote))
                                        self.User1Conn.send(bytes(snd_close1))
                                        sub2Remote.set_n(1)
                                        shunt.shutdown()
                                    else:#
                                        self.User1Conn.send(bytes(snd_close1))
                                end1Vals()
                                self.User1Conn.send(bytes(snd_close1))
                    end1Object()#:)_____________________________________________________________________:(
                client1goodbye()#:)_____________________________________________________________________:(
                endata = str.encode(recvdata, 'utf-8')
                def user1Label():#_________________________________________________________________:(
                    ''' Server sends user double label  to user2 .'''
                    if flashname_a1.get_n() == 1:#
                        flashname_a1.set_n(0)
                        end1Remote.set_n(1)
                        self.User2Conn.send(bytes(flash1+commas+flash1))
                user1Label()#____________________________________________________________________:(
                def service1():#___________________________________________________________________:(
                    '''>>> world.Position to user2  . <<<'''
                    if joinplayer_a2.get_n() == 1:#
                        joinplayer_a1.set_n(1)
                        re1Global.set_n(1)
                        self.User2Conn.send(bytes(endata))
                service1()#______________________________________________________________________:(
                def signal1Label():#_______________________________________________________________:(
                    ''' Server sends user  label  to user2 .'''
                    if spawnPlayer_a3.get_n() == 1:#
                        spawnPlayer_a3.set_n(0)
                        self.User1Conn.send(bytes(user_service1))
                signal1Label()#__________________________________________________________________:(
                def bypass1Remote():#_____________________________________________________________________:(
                    ''' single1User Switchboard .'''
                    if cmd1pass .get_n() == 1:#
                        cmd1pass .set_n(0)
                        main_a1snd.set_n(0)
                        sig1Pass.set_n(1)
                        self.User1Conn.send(bytes(single1User))  
                bypass1Remote()
                def main1():#_____________________________________________________________________:(
                    ''' Main Switchboard .'''
                    if joinplayer_a1.get_n() == 0:#
                        if empty1.get_n() == 1:#
                            empty1.set_n(0)
                            main_a1snd.set_n(0)
                            self.User1Conn.send(bytes(pack_food1))    
                        ''' Single user, no remote  ! '''
                        if selfby1pass.get_n()  == 1:#
                            selfby1pass.set_n(0)
                            main_a1snd.set_n(0)
                            self.User1Conn.send(bytes(snd_bypass))
                        if rigChange.get_n()  == 1:#
                            rigChange.set_n(0)
                            main_a1snd.set_n(0)
                            self.User1Conn.send(bytes(snd_rig1Chg))
                        if main_a1snd.get_n()  == 1:#
                            self.User1Conn.send(bytes(endata))
                        if main_a2snd.get_n()  == 1:#
                            main_a2snd.set_n(0) 
                            self.User1Conn.send(bytes(remote1_raddr))
                        if joinVec1.get_n() == 1:#
                            joinVec1.set_n(0) 
                            self.User1Conn.send(bytes(vector_user1))
                        if ctrl1Opt.get_n() == 1:#
                            ctrl1Opt.set_n(0) 
                            self.User1Conn.send(bytes(ctrl1Opt_user1))
                        if vec1wp.get_n() == 1:#
                            vec1wp.set_n(0) 
                            self.User1Conn.send(bytes(ctrl3Opt_user1))
                        if cont1Opt.get_n() == 1:#
                            cont1Opt.set_n(0) 
                            empty1.set_n(0)
                            self.User1Conn.send(bytes(user_service1))      
                        ''' Server sets users world position . '''
                        if position1User.get_n() == 1:#
                            position1User.set_n(0)
                            self.User2Conn.send(bytes(worldPosistion))
                        if center1Grid.get_n() == 1:#
                            center1Grid.set_n(0)
                            self.User1Conn.send(bytes(center_grid1))
                        if multi1Player.get_n() == 1:#
                            multi1Player.set_n(0)
                            self.User1Conn.send(bytes(pack_multi))   
                        def selfQuit1():#
                            print('>>> main.Register* user1_closing_self.thread .')
                        if  close1Opt.get_n() == 1:#
                            close1Opt.set_n(0)
                            self.User1Conn.send(bytes(whspace))
                            close1Quit = threading.Timer(1.0, selfQuit1)
                            close1Quit.start()
                main1()#___________________:(
                if signal1Off.get_n() == 1:#
                    signal1Off.set_n(0)
                    conn.close()
                    self.resetRegister()
                    break
        except socket.error: #
            print('<<<  user1.Register* disconnection ! >>> ')
            conn.close()
            self.resetRegister()
    def player2_handler(self, conn, addr):#__________________________________________:(
        self.User2Conn = conn
        leave, raddr = addr
        self.player2_raddr = raddr 
        mkco = []
        wspace = []
        bountryRig = '(:)'
        snd_rigBoundry  = str.encode(bountryRig, 'utf-8')
        arenaRig = '(.+.)'
        snd_rigArena = str.encode(arenaRig, 'utf-8')
        rig2Chg = '(|)'
        snd_rig2Chg  = str.encode(rig2Chg, 'utf-8')
        bypass = '<.|'
        snd_bypass  = str.encode(bypass, 'utf-8')
        single2_pass = '<+>'
        single2User = str.encode(single2_pass , 'utf-8')
        remote1user = 'endObject'
        end_remote = str.encode(remote1user, 'utf-8')
        close2 = '>|<'
        snd_close2  = str.encode(close2, 'utf-8')
        client2addr = str(raddr)
        sign2Off = ('clientgoodbye'+client2addr)
        multi = 'multi2'
        pack_multi  = str.encode(multi, 'utf-8')
        food2 = 'packfood'
        pack_food2  = str.encode(food2, 'utf-8')
        grid2 = '+|+'
        center_grid2  = str.encode(grid2, 'utf-8')
        sat1 = 'sat1'
        worldPosistion = str.encode(sat1, 'utf-8')
        opt3 = 'vec_wp'
        ctrl3Opt_user2 = str.encode(opt3, 'utf-8')
        opt2 = 'ctrl'
        ctrl2Opt_user2 = str.encode(opt2, 'utf-8')
        vector2 = '-|-'
        vector_user2 = str.encode(vector2, 'utf-8')
        pipe_break2 = '|'
        pipe2 = str.encode(pipe_break2, 'utf-8')
        raddr_opt2 = str(raddr)
        remote2_raddr = str.encode(raddr_opt2, 'utf-8')
        serv2 = 'global_vectors'
        user_service2 = str.encode(serv2, 'utf-8')
        flash2 = str.encode(self.user2player, 'utf-8')
        pkco = addcomma(mkco)
        commas = str.encode(pkco, 'utf-8')   
        pkspace = whitespace(wspace)
        whspace = str.encode(pkspace, 'utf-8') 
        pinint = byteraddr(raddr) 
        servraddr = str.encode(pinint, 'utf-8')
        def spawner2():#__________________________________________:(
            print(">>> user2.Register* has_started_self.thread !  .*< ")
        spawned2 = threading.Timer(1.0, spawner2)
        spawned2.start()   
        try:#
            thread2Loop.loop2()
            while True:#
                main_b1snd.set_n(1)
                def admin_break2():#
                    if break2loop.get_n() == 1:#
                        break2loop.set_n(0)
                        main_b1snd.set_n(0)
                        main_b2snd.set_n(1) 
                admin_break2()
                def admin_vec2():#
                    if vec2.get_n() == 1:#
                        vec2.set_n(0)
                        joinVec2.set_n(1)
                admin_vec2()
                data = conn.recv(1024)
                recvdata = data.decode("utf-8")
                def client2goodbye():#
                    def end2Object():#___________________________________________________________________:(
                        def end2Vals():#
                            close2User.set_n(0)
                            main_b1snd.set_n(0)
                            close2Opt.set_n(1)
                            signal2Off.set_n(1)
                            re2Global.set_n(0)
                            joinplayer_a2.set_n(0)
                            joinplayer_b2.set_n(0)
                            joinplayer_a1.set_n(0)
                            joinplayer_b1.set_n(0)
                        if close2User.get_n() == 1:#
                            if recvdata == sign2Off:#
                                if sub2Remote.get_n() == 0:#
                                    end2Vals()
                                    if end2Remote.get_n() == 1:#
                                        self.User1Conn.send(bytes(end_remote))
                                        self.User2Conn.send(bytes(snd_close2))
                                        sub1Remote.set_n(1)
                                        shunt.shutdown()
                                    else:#
                                        self.User2Conn.send(bytes(snd_close2))
                                end2Vals()
                                self.User2Conn.send(bytes(snd_close2))
                    end2Object()#:)_____________________________________________________________________:(
                client2goodbye()
                endata = str.encode(recvdata, 'utf-8')
                def user2Label():#_________________________________________________________________:(
                    ''' Server sends user double label  to user1 .'''
                    if flashname_b1.get_n() == 1:#
                        flashname_b1.set_n(0)
                        end2Remote.set_n(1)
                        self.User1Conn.send(bytes(flash2+commas+flash2))
                user2Label()#:)___________________________________________________________________:(
                def service2():#___________________________________________________________________:(
                    '''>>> world.Position to user1  . <<<'''
                    if joinplayer_b2.get_n() == 1:#
                        joinplayer_b1.set_n(1)
                        re2Global.set_n(1)
                        self.User1Conn.send(bytes(endata))
                service2()#:)_____________________________________________________________________:(
                def single2Label():#_______________________________________________________________:(
                    ''' Server sends user label  to user1 .'''
                    if spawnPlayer_b3.get_n() == 1:#
                        spawnPlayer_b3.set_n(0)
                        self.User2Conn.send(bytes(user_service2))
                single2Label()#:)__________________________________________________________________:(
                def bypass2Remote():#_____________________________________________________________________:(
                    ''' single1User Switchboard .'''
                    if cmd2pass .get_n() == 1:#
                        cmd2pass .set_n(0)
                        main_b1snd.set_n(0)
                        self.User2Conn.send(bytes(single2User))  
                bypass2Remote()
                def main2():#_____________________________________________________________________:(
                    ''' Main Switchboard .'''
                    if joinplayer_b1.get_n() == 0:#
                        if empty2.get_n() == 1:#
                            empty2.set_n(0)
                            main_b1snd.set_n(0)
                            self.User2Conn.send(bytes(pack_food2))  
                        ''' Single user, no remote  ! '''
                        if selfby2pass.get_n()  == 1:#
                            selfby2pass.set_n(0)
                            main_b1snd.set_n(0)
                            self.User2Conn.send(bytes(snd_bypass))
                        if main_b1snd.get_n()  == 1:#
                            self.User2Conn.send(bytes(endata))
                        if main_b2snd.get_n()  == 1:#
                            main_b2snd.set_n(0) 
                            self.User2Conn.send(bytes(remote2_raddr))
                        if joinVec2.get_n() == 1:#
                            joinVec2.set_n(0) 
                            self.User2Conn.send(bytes(vector_user2))
                        if ctrl2Opt.get_n() == 1:#
                            ctrl2Opt.set_n(0) 
                            self.User2Conn.send(bytes(ctrl2Opt_user2))
                        if vec2wp.get_n() == 1:#
                            vec2wp.set_n(0) 
                            self.User2Conn.send(bytes(ctrl3Opt_user2))
                        if cont2Opt.get_n() == 1:#
                            cont2Opt.set_n(0)
                            empty2.set_n(0)
                            self.User2Conn.send(bytes(user_service2))  
                        ''' Server sets users world position . '''
                        if position2User.get_n() == 1:#
                            position2User.set_n(0)
                            self.User1Conn.send(bytes(worldPosistion))
                        if center2Grid.get_n() == 1:#
                            center2Grid.set_n(0)
                            self.User2Conn.send(bytes(center_grid2))
                        if multi2Player.get_n() == 1:#
                            multi2Player.set_n(0)
                            self.User2Conn.send(bytes(pack_multi))   
                        def selfQuit2():#
                            print('>>> main.Register* user2_closing_self.thread .')
                        if  close2Opt.get_n() == 1:#
                            close2Opt.set_n(0)
                            self.User2Conn.send(bytes(whspace))
                            close2Quit = threading.Timer(1.0, selfQuit2)
                            close2Quit.start()
                main2()#:)___________________:(
                if signal2Off.get_n() == 1:#
                    signal2Off.set_n(0)
                    conn.close()
                    self.resetRegister()
                    break
        except socket.error: #
            print('<<<  user2.Register* disconnection ! >>> ')
            conn.close()
            self.resetRegister()
    def resetRegister(self):#____________________________________________________________________:(
        def register_user():#_______________:(
            print(">>> *server.Register* reset <<< ")
        cycle.disconnect()
        floatcount()
        def user1_worldPosition():# 
            if joinplayer_a2.get_n() == 1:#
                print(">>> *server.Register* reset_user1_world.Position . <<< ")
                joinplayer_a2.set_n(0)
                joinplayer_a1.set_n(0)
        user1_worldPosition()
        def user2_worldPosition():#
            if joinplayer_b2.get_n()  == 1:#
                print(">>> *server.Register* reset_user2_world.Position . <<< ")
                joinplayer_b2.set_n(0)
                joinplayer_b1.set_n(0)
        user2_worldPosition()
        def singlePassUser():#
              if sig1Pass.get_n() == 1:#
                    sig1Pass.set_n(0)
        #singlePassUser()
        def self_User():#
              if selfuser.get_n() == 1:#
                sig1Pass.set_n(0)
                selfuser.set_n(0)
        self_User()
        def self_Remote():#
              if selfremote.get_n() == 1:#
                  selfremote.set_n(0)              
        self_Remote()
        registerReset = threading.Timer(1.0, register_user)
        registerReset.start()
    def Main_Register(self, conn, addr, count):#____________________________________________________:(
        def register_user():#_________________:(
            print(">>> server.Registering* new_user ? <<< ")
        leave, raddr = addr
        mkco = []
        wspace = []
        pinint = byteraddr(raddr) 
        pkco = addcomma(mkco)
        pkspace = whitespace(wspace)
        servraddr = str.encode(pinint, 'utf-8')
        commas = str.encode(pkco, 'utf-8')        
        whspace = str.encode(pkspace, 'utf-8') 
        try:#
            while True:#
                data = conn.recv(1024)
                recvdata = data.decode("utf-8")
                endata = str.encode(recvdata, 'utf-8')
                conn.send(bytes(endata+commas+servraddr+whspace))
                break
                if not data:#
                    conn.close()
                    break
            self.config_users.append(recvdata)
            registerUser = threading.Timer(1.0, register_user)
            registerUser.start()
        except socket.error: #
            print('<<<  user.Register* disconnection ! >>> ')
            conn.close()
        if floatcount.get_n() ==  1:#
            usersRegister.set_n(1)
            sub1Remote.set_n(0)
            id1User.set_n(1)
            end1Remote.set_n(0) 
            close1User.set_n(1)
            bindport1.set_n(1)
            user1 = threading.local()
            user1.a1 = recvdata
            data = str.encode(user1.a1, 'utf-8')
            self.user1player = data.decode("utf-8")
        if floatcount.get_n() ==  2:#
            usersRegister.set_n(1)
            sub2Remote.set_n(0)
            id2User.set_n(1)
            end2Remote.set_n(0)
            close2User.set_n(1)
            bindport2.set_n(1)
            user2 = threading.local()
            user2.b1 = recvdata            
            data = str.encode(user2.b1, 'utf-8')
            self.user2player = data.decode("utf-8") 
    def run(self):#__________________________________________________________________________:(
        ''' Let the Threading Begin ! '''
        def hello_admin():#___________:(
            print(">>> Hello_admin_register . <<< ")
        def registered_user1():#_________:(
            print(">>> Hello_register_user1 . >>> ")
        def registered_user2():#_________:(
            print(">>> Hello_register_user2 . >>> ")
        def player1_intro():#_______________:(
            print(">>> user1 > stand-by ! >>> ")
        def player2_intro():#_______________:(
            print(">>> user2 > stand-by ! >>> ")
        while True:#
            ''' The only way out is the exits or disconnections  . '''
            conn, addr = self.serv.accept()
            conn.settimeout(None)
            if adminUser.get_n() == 0:#
                floatcount.set_n(0)
                adminUser.set_n(1)
                admin1Thread = threading.Thread(target = self.admin_handler, args = (conn, addr))
                admin1Thread.daemon = True
                admin1Thread.start()
                admin = threading.Timer(1.0, hello_admin)
                admin.start()       
            if usersRegister.get_n() == 1:#
                usersRegister.set_n(0)
                cycle.count()
                setbit = floatcount.get_n()
                floatcount.set_n(setbit)
                count = floatcount.get_n() 
                self.Main_Register(conn, addr, count)
                if bindport1.get_n() == 1:#
                    bindport1.set_n(0)
                    player1.set_n(1)# 
                    register1 = threading.Timer(1.0, registered_user1)
                    register1.start()
                if bindport2.get_n() == 1:#
                    bindport2.set_n(0)
                    player2.set_n(1)#
                    register2 = threading.Timer(1.0, registered_user2)
                    register2.start()
            if player1.get_n()  == 1:#
                player1.set_n(0)
                port1Thread1 = threading.Thread(target = self.player1_handler, args = (conn, addr))
                port1Thread1.daemon = True
                port1Thread1.start()
                user1 = threading.Timer(1.0, player1_intro)
                user1.start()
                selfuser.set_n(1)#< < <
            if player2.get_n()  == 1:#
                player2.set_n(0)
                port2Thread2 = threading.Thread(target = self.player2_handler, args = (conn, addr))
                port2Thread2.daemon = True
                port2Thread2.start()
                user2 = threading.Timer(1.0, player2_intro)
                user2.start()         
                selfremote.set_n(1)#< < <
class Cycle:#_____________________________________________________________________________:(
    def __init__(self):#
        self.cyc = 0
    def count(self):#
        self.cyc = floatcount.get_n() + 1
        floatcount.set_n(self.cyc)
    def disconnect(self):#
        out = floatcount.get_n() - 1
        floatcount.set_n(out)
class Step:#_____________________________________________________________________________:(
    def __init__(self):#
        self.stp1 = 0
        self.stp2 = 0
    def place1(self):#
        self.stp1 = float1stp.get_n() + 1
        float1stp.set_n(self.stp1)
    def place2(self):#
        self.stp2 = float2stp.get_n() + 1
        float2stp.set_n(self.stp2)
class NameUpdate:#_______________________________________________________________________:(
    def __init__(self):#
        ''' clock in the users 1, 2, etc . '''
        self.tag = 0
    def player(self):#
        self.tag = refresh.get_n() +1
        refresh.set_n(self.tag)
class GetUpdate:#_________________________________________________________________________:(
    def __init__(self):#
        ''' clock in the users 1, 2, etc . '''
        self.getname = 0
    def player(self):#
        self.getname = refreshOut.get_n() +1
        refresh0ut.set_n(self.getname)
class Thread1Loop:#________________________________________________________________________:(
    def __init__(self):#
        self.loops1 = 0
    def loop1(self):#
        self.loops1 = loops1.get_n() + 1
        loops1.set_n(self.loops1)
    def deloop1(self):#
        out = loops1.get_n() - 1
        loops1.set_n(out)
class Thread2Loop:#_________________________________________________________________:(
    def __init__(self):#
        self.loops2 = 0
    def loop2(self):#
        self.loops2 = loops2.get_n() + 1
        loops2.set_n(self.loops2)
    def deloop2(self):#
        out = loops2.get_n() - 1
        loops2.set_n(out)
class Thread3Loop:#___________________________________________________________________:(
    def __init__(self):#
        self.loops3 = 0
    def loop3(self):#
        self.loops3 = loops3.get_n() + 1
        loops3.set_n(self.loops3)
class Shunt:#_____________________________________________________________________________:(
    def __init__(self):#
        self.sht = 0
    def shutdown(self):#
        self.sht = shuntcount.get_n() + 1
        shuntcount.set_n(self.sht)
''' Channels  : vals'''
ch1nl = Ch1nl() 
ch2nl = Ch2nl() 
ch3nl = Ch3nl() 
sig1nl = Sig1nl() 
sig2nl =Sig2nl() 
sig3nl = Sig3nl() 
''' class Server()_________________________________________________________________________________________________'''
server = Server()
''' class Cycle()__________________________________________________________________________________________________'''
cycle = Cycle()
''' Cycle()   : vals'''
floatcount = Floatcount()
''' class Step()___________________________________________________________________________________________________'''
step = Step()
''' Step()  : vals'''
float1stp = Float1stp()
float2stp = Float2stp()
''' class NameUpdate()____________________________________________________________________________________________'''
nameUpdate = NameUpdate()
''' NameUpdate()   : vals'''
refresh = Refresh()
''' class GetUpdate() _____________________________________________________________________________________________'''
getUpdate = GetUpdate()
''' GetUpdate()  : vals'''
refresh0ut = Refresh0ut()
''' class Thread1Loop()_____________________________________________________________________________________________'''
thread1Loop = Thread1Loop()
''' Thread1Loop() : vals'''
loops1 = Loops1()
''' class Thread2Loop()_____________________________________________________________________________________________'''
thread2Loop = Thread2Loop()
''' Thread2Loop() : vals'''
loops2 = Loops2()
''' class Thread3Loop()_____________________________________________________________________________________________'''
thread3Loop = Thread3Loop()
''' Thread3Loop() : vals'''
loops3 = Loops3()
''' values '''
admin = Admin()
player1 = Player1()
player2 = Player2()
''' class Shunt()_____________________________________________________________________________________________'''
shunt = Shunt()
''' values '''
shuntcount = ShuntCount()
''' Admins . . .Ctrl . . . . .'''
adminUser = Terminallock1()
admin1Spawn = Admin1Spawn()
admin2Spawn = Admin2Spawn()
usersRegister = UsersRegister()
''' server ctrl locks . '''
rec_a1 = Rec_a1()
snd_a1 = Snd_a1()
rec_b1 = Rec_b1()
snd_b1 = Snd_b1()
''' server ctrl lks . '''
''' users ctrl lks .'''
joinplayer_a1 = Joinplayer_a1()
joinplayer_a2 = Joinplayer_a2()
spawnPlayer_a3 = SpawnPlayer_a3()
joinplayer_b1 = Joinplayer_b1()
joinplayer_b2 = Joinplayer_b2()
spawnPlayer_b3 = SpawnPlayer_b3()
''' users ctrl lks .'''
''' class Server()  '''
'''  server binders .'''
bindport1 = Bindport1()
bindport2 = Bindport2()
binduser1 = Binduser1()
binduser2 = Binduser2()
'''  server binders .'''
refresh0ff = Refresh0ff()
nameUpdater = NameUpdater()
refresh0n = Refresh0n()
floatplayer1 = FloatPlayer1()
floatplayer2 = FloatPlayer2()
player1Name = Player1Name()
player2Name = Player2Name()
''' Flash : for socket sending testbits ? '''
flashname_a1 = Flashname_a1()
flashname_b1 = Flashname_b1()
spawners1 = Spawners1()
spawners2 = Spawners2()
spawn_a1 = Spawn_a1()
spawn_b1 = Spawn_b1()
snda1msg = Snda1msg()
sndb1msg = Sndb1msg()
begin1Spawn = Begin1Spawn()
begin2Spawn = Begin2Spawn()
optsnd1 = Optsnd1()
optsnd2 = Optsnd2()
recv1Avatar = Recv1Avatar()
recv2Avatar = Recv2Avatar()
avatar_a1 = Avatar1user()
avatar_b1 = Avatar2user()
empty = Empty()
tmp = Tmp()
temp = Temp()
cont1Opt = Cont1Opt()
cont2Opt = Cont2Opt()
main_a1snd = Main_a1snd()  
main_a2snd = Main_a2snd()
main_b1snd = Main_b1snd()
main_b2snd = Main_b2snd()
break1loop = Break1Loop()
break2loop = Break2Loop()
vec1 = Vec1()
vec2 = Vec2()
joinVec1 = JoinVec1()
joinVec2 = JoinVec2()
ctrlVec1 = CtrlVec1() 
ctrlVec2 = CtrlVec2() 
ctrl1Opt = Ctrl1Opt()
ctrl2Opt = Ctrl2Opt()
vec1wp = Vec1Wp()
vec2wp = Vec2Wp()
empty1 = Empty1()
empty2 = Empty2()
cont1Opt = Cont1Opt()
cont2Opt = Cont2Opt()
position1User = Position1User()
position2User = Position2User()
center1Grid = Center1Grid()
center2Grid = Center2Grid()
multi1Player = Multi1Player()
multi2Player = Multi2Player()
close1User = Close1User()
close2User = Close2User()
signal1Off = Signal1Off()
signal2Off = Signal2Off()
close1Opt = Close1Opt()
close2Opt = Close2Opt()
quit1 = Quit1()
quit2 = Quit2()
selfuser = SelfUser()
selfremote = SelfRemote()
selfby1pass = SelfBy1Pass()
selfby2pass = SelfBy2Pass()
cmdpass = CmdPass()
cmd1pass = Cmd1Pass()
cmd2pass = Cmd2Pass()
cmd3pass = Cmd3Pass()
cmd4pass = Cmd4Pass()
cmd5pass = Cmd5Pass()
cmd5pass = Cmd6Pass()
cmd7pass = Cmd7Pass()
end1Remote =  End1Remote()
end2Remote =  End2Remote()
sub1Remote = Sub1Remote() 
sub2Remote = Sub2Remote() 
cmd1Post = Cmd1Post()
cmd2Post = Cmd2Post()
cmd1run = Cmd1Run()
idself1User = IdSelf1User()
idself2User = IdSelf2User()
id1User = Id1User()
id2User = Id2User()
re1Global = re1Global()
re2Global = re2Global()
rigChange = RigChange()
arena1Opt = Arena1Opt() 
arena2Opt = Arena2Opt() 
boundry1Opt  = Boundry1Opt()
boundry2Opt  = Boundry2Opt()
sig1Pass = Sig1Pass()
server.run()
###############################################################################
