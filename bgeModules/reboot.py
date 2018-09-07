# !/usr/bin/env python .
# Created Monday, August 27, 2018 .
# Blender 2.79 reboot.py
# 
# Last update : 
###########################################
import socket
#import config
#import clientconfig
#import configdeltas
ipser = (socket.gethostbyname(socket.gethostname()))
server_ip = ipser
server_port = 12346
reboot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
###########################################
class Main:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Main' property.")
main = Main()
############
def returns():#_________________________________________________:(
    while True:#
        try:#
            data = reboot.recv(1024)
            if data:#
                recvdata = data.decode("utf-8")
            break
        except reboot.error:#
            pass
            break   
def filesystem():#_________________________________________________:(
    reboot.connect((server_ip, server_port))
    reboot.send(b'Z3N0YXI=')
    returns()
##    snd_data = b'Z3N0YXI='
##    msg = str.encode(snd_data, 'utf-8')
##    register.send(bytes(msg))
##    startUpCheck()


