# !/usr/bin/env python .
# Created Tuesday, September 4, 2018 .
# Blender 2.79 empty.py
# 
# Last update :
# 
# 
#
#
#
#
#
#
import clientutils
import serveruser
import incident
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
#       
    def packet(self):#_____________b'Z3N0YXI='_________________________:(


        loader.setx(incident.cmdpass.setx())        
        codec = clientutils.EncodeServer(loader.getx())#
        inventory.send(codec)
        returns()

def returns():#_________________________________________________:(

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
