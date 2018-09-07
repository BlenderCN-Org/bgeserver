# !/usr/bin/env python .
# Created Saturday, August 11, 2018 .
# Blender 2.79 dictclient.py
# 
# Last update :
import configdeltas
import scheduleclient
import servers
dict_pack = []
list_pack = []
def Login(listing_key):#
    listing = {
        0: 'login',
        1: 'client',
        2: 'user',
        3: 'player1',
        4: 'player2' ,
        5: 'login',
        6: 'login' ,
    }
    return listing[listing_key]#
def ServerCommands(listing_key):#
    listing = {
        0: 'active',
        1: 'op',
        2: 'pip',
        3: 'wp' ,
        4: 'sat',
        5: 'fas' ,
        6: 'glob' ,
    }
    return listing[listing_key]#
def Schedules(listing_key):#
    listing = {
        0: 'sch0',
        1: 'sch1',
        2: 'sch2',
        3: 'sch3',
        4: 'sch4',
        5: 'sch5',
        6: 'sch6' ,
    }
    return listing[listing_key]#
def DirectoryAssembly(listing_key):#
    listing = {
        0: 'rig',
        1: 'mesh',
        2: 'cam',
        3: 'controls',
        4: 'viewports',
        5: 'spawners',
        6: 'aux',
    }
    return listing[listing_key]#
def Functions(listing_key):#
    listing = {
        0: 'func0',
        1: 'faccess',
        2: 'fload',
        3: 'fsave',
        4: 'reload' ,
        5: 'func5',
        6: 'func6' ,
    }
    return listing[listing_key]#
def ViewPorts(listing_key):#
    listing = {
        0: 'front',
        1: 'back',
        2: 'right',
        3: 'left',
        4: 'rightcorner',
        5: 'leftcorner',
        6: 'spawner',
    }
    return listing[listing_key]#
def Mouse(listing_key):#
    listing = {
        0: 'mload',
        1: 'Rclick',
        2: 'Lclick',
        3: 'over',
        4: 'wheel' ,
        5: 'up',
        6: 'down' ,
    }
    return listing[listing_key]#
def dict_Login():#_.........
    configdeltas.deletelogin(1)
    for k in range(7):#_____________________
        dict_pack = Login(k)#
        list_pack.append(dict_pack)
    return list_pack
def dict_ServerCommands():#_.........
    configdeltas.deleteserver(1)
    servers.main.setx(1)
    for k in range(7):#_____________________
        dict_pack = ServerCommands(k)#
        list_pack.append(dict_pack)
    return list_pack
        #
def dict_Schedules():#_.........
    configdeltas.deleteschedules(1)
    scheduleclient.asmy.setx(1)
    for k in range(7):#_____________________
        dict_pack = Schedules(k)#
        list_pack.append(dict_pack)
    return list_pack
        #
def dict_DirectoryAssembly():#_.........
    configdeltas.deleteassembly(1)
    for k in range(7):#_____________________
        dict_pack = DirectoryAssembly(k)#
        list_pack.append(dict_pack)
    return list_pack
        #
def dict_Functions():#_.........
    configdeltas.deletefunctions(1)
    for k in range(7):#_____________________
        dict_pack = Functions(k)#
        list_pack.append(dict_pack)
    return list_pack#
        #
def dict_ViewPorts():#_.........
    configdeltas.deleteviewport(1)
    for k in range(7):#_____________________
        dict_pack = ViewPorts(k)#
        list_pack.append(dict_pack)
    return list_pack#
def dict_Mouse():#_.........
    configdeltas.deletemouse(1)
    for k in range(7):#_____________________
        dict_pack = Mouse(k)#
        list_pack.append(dict_pack)
    return list_pack#
