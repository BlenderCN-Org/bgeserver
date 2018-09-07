# !/usr/bin/env python .
# Created Friday, June 22, 2018 .
# Blender 2.79 registername.py
# 
# Last update :
import socket
import config
import idclient
import remoteregister
import remotename
import username
import remoteconfig
import clientname
import remoteuser
import clientconfig
##import esc
##import initenter
ipser = (socket.gethostbyname(socket.gethostname()))
server_ip = ipser
server_port = 12345
register = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def cleanlist1(list1):#_____________________________:(
    return str(list1).replace('', '(').replace('', ')')
def startUpClient():#________________One_______________________________:(
    ''' Start Scene ... Client is Ready .'''
    while True:#
        try:#___________________________:(
            data = register.recv(1024)
            if data:#
                state = data.decode("utf-8")
                list1 = state
                clist = cleanlist1(list1)
                lenslpit = len(clist)
                valsplit = state.split(',',lenslpit)
                name, raddr = valsplit
                config.setAddress(int(raddr))
                config.setName(str(name))
                clientconfig.enterClientOp(1)
                break
            break
        except register.error:#
            pass
            break
def returnCloseClient():#____________________________End______________________________:(
    while True:#
        try:#__________________________:(
            data = register.recv(1024)
            if data:#________________________:(
                recvdata = data.decode("utf-8")
                if recvdata == '>|<':#
                    config.closeClient(1)
                    idclient.setLogOff(1)
                break
        except register.error:#
            pass
            break
def returns():#_________________________________________________:(
    while True:#
        try:#
            data = register.recv(1024)
            if data:#
                recvdata = data.decode("utf-8")
            break
        except register.error:#
            pass
            break    
def registerClient():#_________________________________________________:(
    register.connect((server_ip, server_port))
    snd_data = 'Suzanne'
    msg = str.encode(snd_data, 'utf-8')
    register.send(bytes(msg))
    startUpClient()
def closeClient():#__________________________________________________________:(
    returnAdress = config.getAddress(config)
    snd_data = ('clientgoodbye'+str(returnAdress))
    msg = str.encode(snd_data, 'utf-8')
    register.send(bytes(msg))
    returnCloseClient()
def checkPoint():#__________________________________________________________:(
    def gladmsg():#
        ''' Find out more from www.HTTP///pythonservers. '''
        ''' BGE User/Client Physics Engine 2018 . '''
        snd_data = '|'
        msg = str.encode(snd_data, 'utf-8')
        register.send(bytes(msg))
    gladmsg()
    while True:#______________________
        try:#___________________________
            data = register.recv(1024)
            recvdata = data.decode("utf-8")
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
                    clientconfig.enterClientPip(1)
                    break
            break 
        except register.error:#
            pass
            break  
def connected():#_________________________________________________________________:(
    def clientmsg():#
        snd_data = ' >>>* Now Connected Online with Server ! '
        msg = str.encode(snd_data, 'utf-8')
        register.send(bytes(msg))
    clientmsg()
    while True:#______________________
        try:#___________________________
            data = register.recv(1024)
            if data:#
                recvdata = data.decode("utf-8")
                lenslpit = len(recvdata)
                valsplit = recvdata.split(',',lenslpit)
                valuedate = len(valsplit)
            if valuedate == 2:#
                label1, label2 = valsplit
                #clientconfig.enterClientOp(1)
                clientname.enterName(str(label1)+str(label2))
                break
        except register.error:#
            pass
            break
def worldPosition():#_____________________________________________________________:(
    def wpmsg():#
        snd_data = '|.>'
        msg = str.encode(snd_data, 'utf-8')
        register.send(bytes(msg))
    wpmsg()
    while True:#
        release_ctrl2 = '|.>vec_wp'
        try:#__________________________:(
            data = register.recv(1024)
            if data:#________________________:(
                recvdata = data.decode("utf-8")
                if recvdata == release_ctrl2:#
                    '''>>> locate.Satilites.position . <<<'''
                    clientconfig.enterClientWp(1)
                    break
            break
        except register.error:#
            pass
            break   
def imageFactory():#_____________________________________________________________:(
    ''' ["sat"] = satillites : get objects from server, Image Factory, Polygon Factory '''
    def satmsg():#
        snd_data = '<.|'
        msg = str.encode(snd_data, 'utf-8')
        register.send(bytes(msg))
    satmsg()
    while True:#
        release_ctrl5 = '<.|sat1'
        try:#__________________________:(
            data = register.recv(1024)
            if data:#________________________:(
                recvdata = data.decode("utf-8")
                if recvdata == release_ctrl5:#
                    clientconfig.enterClientSat(1)
                    break
            break
        except register.error:#
            pass
            break 
def connectCheck():#_____________________________________________________________:(
    ''' ["fas"] = checks for satillite servers online or not .'''
    def flashmsg():#
        snd_data = '<.|'
        msg = str.encode(snd_data, 'utf-8')
        register.send(bytes(msg))
    flashmsg()
    while True:#
        try:#__________________________:(
            data = register.recv(1024)
            if data:#________________________:(
                recvdata = data.decode("utf-8")
                clientconfig.enterClientFas(1)
                break
            break
        except register.error:#
            pass
            break 
def coordinates():#_____________________________________________________________:(
    ''' ["glob"] = global position in world, sends User coordinates to Server .'''
    def globmsg():#
        snd_data = '<.|'
        msg = str.encode(snd_data, 'utf-8')
        register.send(bytes(msg))
    globmsg()
    while True:#
        try:#__________________________:(
            data = register.recv(1024)
            if data:#________________________:(
                recvdata = data.decode("utf-8")
                clientconfig.enterClientGlob(1)
                break
            break
        except register.error:#
            pass
            break 
