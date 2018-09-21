# !/usr/bin/env python .
# Created Monday, August 27, 2018 .
# Blender 2.79 filesys.py
# 
# Last update : 
################
import socket

#ipser = (socket.gethostbyname(socket.gethostname()))
ipser = "192.168.2.51"
server_ip = ipser
server_port = 12346
inventory = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
import clientutils
import iduser
import serveruser
import incident
################
###########################################
##########################################
class Main:#
    def __init__(self):#
        self._x = None
    def getx(self):#
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Main' property.")
main = Main()
############
#
############
class Loader:#
    def __init__(self):#
        self._x = None
    def getx(self):#
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Loader' property.")
loader = Loader()
############
#
############
class Packet:#
    def __init__(self):# assets
        self._x = None
    def getx(self):#
        assets.packet()
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Packet' property.")
packet = Packet()
############
#
############
class LabelFile:#
    def __init__(self):#
        self._x = None
    def getx(self):#
        assets.namelabel()
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'LabelFile' property.")
labelfile= LabelFile()
########
#
#############
class StartServer:#
    def __init__(self):#
        self._x = None
    def getx(self):#
        assets.startserver()
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'StartServer' property.")
startserver = StartServer()
########
#
#############
class FileSystem:#
    def __init__(self):#
        self._x = None
    def getx(self):#
        assets.filesystem()
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'FileSystem' property.")
filesystem = FileSystem()
########
#
#####################
class Incident:#
    def __init__(self):#
        self._x = None
    def getx(self):#
        return self._x
    def setx(self, value):#
        self._x = value
    def delx(self):#
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'Incident' property.")
incident = Incident()
########
#
#####################
def Response(listing_key):#
    listing = {
        0: 'start',
        1: 'msg',
        2: 'empty',
        3: 'empty',
        4: 'empty',
        5: 'empty',
        6: 'empty',
        }
    return listing[listing_key]#
def dict_Response():#_.........
    idserv.main.setx(1)
    for k in range(7):#_____________________
        dict_pack = Response(k)#
        list_pack.append(dict_pack)
    return list_pack   
######################
class ServerError(Exception):#
    def __init__(self, message):#
        self.message = message
#
class Assets:#_____________________:(

    def __init__(self):#

        self.codec = []

    def startserver(self):#

        inventory.connect((server_ip, server_port))       

    def namelabel(self):#_________________________________________________:(

        loader.setx(iduser.initUserEnd(iduser))
        
    def packet(self):#_____________b'Z3N0YXI='_________________________:(
        
        self.codec = clientutils.EncodeServer(loader.getx())#

    def incidentreplies(self):#_____________b'Z3N0YXI='_________________________:(
        
        self.codec = clientutils.EncodeServer(incident.getx())#

    def filesystem(self):#________________________________________________:(

        inventory.send(self.codec)
        self.returns()
        
    def returns(self):#_________________________________________________:(

        while True:#
            try:#
                data = inventory.recv(1024)
                if data:#
                    recvdata = data.decode("utf-8")
                    serveruser.mainreturns.setx(recvdata)

                break
            except inventory.error:#
                pass
                break    
#############                                 
assets=Assets()
##############
