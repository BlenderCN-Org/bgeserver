# !/usr/bin/env python .
# Created Friday, June 15, 2018 .
# Blender 2.79 user.py
# 
# Last update : Tuesday, June 26
import socket
import log
import ctrl
import request
import rtn
import esc
import initenter
import config
import initremote
import remoteconfig
import username
import remotename
import clientconfig
ipser = (socket.gethostbyname(socket.gethostname()))

server_ip = ipser
server_port = 12345
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((server_ip, server_port))
def cleanlist1(list1):#_____________________________:(
    return str(list1).replace('', '(').replace('', ')')
def startUpClient():#________________One_______________________________:(
    ''' Start Scene ... Client is Ready .'''
    while True:#
        try:#___________________________:(
            data = socket.recv(1024)
            if data:#
                state = data.decode("utf-8")
                list1 = state
                clist = cleanlist1(list1)
                lenslpit = len(clist)
                valsplit = state.split(',',lenslpit)
                name, raddr = valsplit
                config.setAddress(int(raddr))
                config.setName(str(name))
                esc.setEsc(1)
                initremote.setEnter(1)
                remoteconfig.enterRemoteOp(1)
                break
            break
        except socket.error:#
            pass
            break
def singleReturns():#_________________________________________________:(
    while True:#
        try:#
            data = socket.recv(1024)
            if data:#
                recvdata = data.decode("utf-8")
                ctrl.setClient(0)
                esc.setEsc(1)
                initenter.setEnter(1)
                break
        except socket.error:#
            pass
            break    
def requestReturns():#_________________________________________________:(
    while True:#
        try:#
            data = socket.recv(1024)
            if data:#
                recvdata = data.decode("utf-8")
                ctrl.setClient(0)
                rtn.setCtrl(1)
                request.setRequest(recvdata)
                break
        except socket.error:#
            pass
            break    
def logSingle():#___________  Admin Register ______________________________________:(
    snd_data = 'user'
    msg = str.encode(snd_data, 'utf-8')
    socket.send(bytes(msg))
    singleReturns()

def logMulti():#______________Second Client Register___________________________________:(
    snd_data = 'Remote'
    msg = str.encode(snd_data, 'utf-8')
    socket.send(bytes(msg))
    startUpClient()

def logRequest():#_____________Console Returns____________________________________:(
    socket.send(log.getClient(log))
    requestReturns()#
def checkPoint():#
    def gladmsg():#
        ''' Find out more from www.HTTP///pythonservers. '''
        ''' BGE User/Client Physics Engine 2018 . '''
        snd_data = '|'
        msg = str.encode(snd_data, 'utf-8')
        socket.send(bytes(msg))
    gladmsg()
    while True:#______________________
        try:#___________________________
            data = socket.recv(1024)
            recvdata = data.decode("utf-8")
            username.enterName(str(recvdata))
            value = recvdata
            if value:#
                data = recvdata.strip()
                a = data
                b = config.getAddress(config)
                list_a = list(str(a))
                list_b = list(str(b))
                c=len(str(a))
                d=len(str(b))
                if c == d:#
                    remoteconfig.enterRemotePip(1)
                    break
            break 
        except socket.error:#
            pass
            break      
def connected():#_________________________________________________________________:(
    ''' ["op"] = operator : Server returns other players name label . '''
    def remotemsg():#
        snd_data = ' >>> * Now Connected Online with Server ! <<< '
        msg = str.encode(snd_data, 'utf-8')
        socket.send(bytes(msg))
    remotemsg()
    while True:#______________________
        try:#___________________________
            data = socket.recv(1024)
            if data:#
                recvdata = data.decode("utf-8")
                lenslpit = len(recvdata)
                valsplit = recvdata.split(',',lenslpit)
                valuedate = len(valsplit)
            if valuedate == 2:#
                label1, label2 = valsplit
                #remoteconfig.enterRemoteOp(1)
                username.enterName(str(label1)+str(label2))
                break
        except socket.error:#
            pass
            break
def worldPosition():#_____________________________________________________________:(
    ''' ["wp"] : set world position in Scene .'''
    def wpmsg():#
        snd_data = '|.>'
        msg = str.encode(snd_data, 'utf-8')
        socket.send(bytes(msg))
    wpmsg()
    while True:#
        release_ctrl2 = '|.>vec_wp'
        try:#__________________________:(
            data = socket.recv(1024)
            if data:#________________________:(
                recvdata = data.decode("utf-8")
                if recvdata == release_ctrl2:#
                    remoteconfig.enterRemoteWp(1)
                    username.enterName(str(recvdata))
                    break
            break
        except socket.error:#
            pass
            break 
def imageFactory():#_____________________________________________________________:(
    ''' ["sat"] = satillites : Get objects from server, Image Factory, Polygon Factory '''
    def satmsg():#
        snd_data = '<.|'
        msg = str.encode(snd_data, 'utf-8')
        socket.send(bytes(msg))
    satmsg()
    while True:#
        release_ctrl5 = '<.|sat1'
        try:#__________________________:(
            data = socket.recv(1024)
            if data:#________________________:(
                recvdata = data.decode("utf-8")
                if recvdata == release_ctrl5:#
                    remoteconfig.enterRemoteSat(1)
                    username.enterName(str(recvdata))
                    break
            break
        except socket.error:#
            pass
            break 
def connectCheck():#_____________________________________________________________:(
    ''' ["fas"] = checks for satillite servers online or not .'''
    def flashmsg():#
        snd_data = '<.|flash'
        msg = str.encode(snd_data, 'utf-8')
        socket.send(bytes(msg))
    flashmsg()
    while True:#
        try:#__________________________:(
            data = socket.recv(1024)
            if data:#________________________:(
                recvdata = data.decode("utf-8")
                remoteconfig.enterRemoteFas(1)
                username.enterName(str(recvdata))
                break
            break
        except socket.error:#
            pass
            break 
def coordinates():#_____________________________________________________________:(
    ''' ["glob"] = global position in world, sends User coordinates to Server .'''
    def globmsg():#
        snd_data = '<.|global'
        msg = str.encode(snd_data, 'utf-8')
        socket.send(bytes(msg))
    globmsg()
    while True:#
        try:#__________________________:(
            data = socket.recv(1024)
            if data:#________________________:(
                recvdata = data.decode("utf-8")
                remoteconfig.enterRemoteGlob(1)
                username.enterName(str(recvdata))
                break
            break
        except socket.error:#
            pass
            break 
##                        globalOpt.set_n(1)
##                        streamMsg.set_n(1)
##                        streamOpt.set_n(1)
##        release_ctrl4 = '<.|global_vectors'
##        release_ctrl5 = '<.|sat1'
##        release_ctrl7 = 'run'
##        release_ctrl8 = 'endObject'
''' ["multi1, multi2"] = set player one & two Viewport and Keyboard Character controls .'''
''' ["ctrl"] = control : User Command functions for players choice .'''

''' command shell type : bypass : pass1 : rig1 < " for single User ! '''
#
