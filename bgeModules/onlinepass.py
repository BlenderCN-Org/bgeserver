# !/usr/bin/env python .
# Created Friday, June 22, 2018 .
# Blender 2.79 onlinepass.py
# 
# Last update :
import socket
import ctrl
ipser = (socket.gethostbyname(socket.gethostname()))
def setConnection():#
    server_ip = ipser
    server_port = 12345
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((server_ip, server_port))
def onlineSingle():#_________________________________________________:(
    snd_data = 'user'
    msg = str.encode(snd_data, 'utf-8')
    socket.send(bytes(msg))
    onlineReturns()
def onlineMulti():#_________________________________________________:(
    snd_data = 'reset'
    msg = str.encode(snd_data, 'utf-8')
    socket.send(bytes(msg))
    onlineReturns()
def onlineReturns():#_________________________________________________:(
    while True:#
        try:#
            data = socket.recv(1024)
            if data:#
                recvdata = data.decode("utf-8")
                ctrl.setClient(0)
                break
        except:#
            pass
