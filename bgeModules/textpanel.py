# !/usr/bin/env python .
# Created Wednesday, August 15, 2018 .
# Blender 2.79 textpanel.py
# Dictionary Loader .
# Last update :
import ackpanel
#
class PanelPlate:#

    def __init__(self):#___________________Monday June 4 2018 Installed . ___________________________________________:(

        self.plate = 0

    def mainHeader(self):#
        #print(' >>> panel.0 main.Header .')#

        ackpanel.minLocX.setx(33 + ackpanel.viewPortX.getx())
        ackpanel.maxLocX.setx(135 + ackpanel.viewPortX.getx())
        ackpanel.minLocY.setx(16 + ackpanel.viewPortY.getx())
        ackpanel.maxLocY.setx(65 + ackpanel.viewPortY.getx())
        ackpanel.index.setx("ackMain")

    def mouseEnter(self):#
        #print(' >>> panel.1 mouse.Enter .')

        ackpanel.minLocX.setx(501 + ackpanel.viewPortX.getx())
        ackpanel.maxLocX.setx(616 + ackpanel.viewPortX.getx())
        ackpanel.minLocY.setx(361 + ackpanel.viewPortY.getx())
        ackpanel.maxLocY.setx(383 + ackpanel.viewPortY.getx())
        ackpanel.index.setx("ackEnter")

    def mouseExit(self):#
        #print(' >>> panel.2 mouse.Exit.')

        ackpanel.minLocX.setx(674 + ackpanel.viewPortX.getx())
        ackpanel.maxLocX.setx(781 + ackpanel.viewPortX.getx())
        ackpanel.minLocY.setx(361 + ackpanel.viewPortY.getx())
        ackpanel.maxLocY.setx(383 + ackpanel.viewPortY.getx())
        ackpanel.index.setx("ackExit")

    def serverStart(self):#
        #print(' >>> panel.5 server.Start .')

        ackpanel.minLocX.setx(33 + ackpanel.viewPortX.getx())
        ackpanel.maxLocX.setx(131 + ackpanel.viewPortX.getx())
        ackpanel.minLocY.setx(160 + ackpanel.viewPortY.getx())
        ackpanel.maxLocY.setx(221 + ackpanel.viewPortY.getx())
        ackpanel.index.setx("ackServer")

    def meshesRigsClient(self):#
        #print(' >>> panel.6 meshesRigs.Client .')

        ackpanel.minLocX.setx(33 + ackpanel.viewPortX.getx())
        ackpanel.maxLocX.setx(131 + ackpanel.viewPortX.getx())
        ackpanel.minLocY.setx(260 + ackpanel.viewPortY.getx())
        ackpanel.maxLocY.setx(310 + ackpanel.viewPortY.getx())
        ackpanel.index.setx("ackMeshesRigs")

    def arenaClient(self):#
        #print(' >>> panel.7 arena.Client .')

        ackpanel.minLocX.setx(33 + ackpanel.viewPortX.getx())
        ackpanel.maxLocX.setx(131 + ackpanel.viewPortX.getx())
        ackpanel.minLocY.setx(325 + ackpanel.viewPortY.getx())
        ackpanel.maxLocY.setx(390 + ackpanel.viewPortY.getx())
        ackpanel.index.setx("ackArena")

    def projectClient(self):#
        #print(' >>> panel.8 project.Client .')

        ackpanel.minLocX.setx(33 + ackpanel.viewPortX.getx())
        ackpanel.maxLocX.setx(131 + ackpanel.viewPortX.getx())
        ackpanel.minLocY.setx(440 + ackpanel.viewPortY.getx())
        ackpanel.maxLocY.setx(490 + ackpanel.viewPortY.getx())
        ackpanel.index.setx("ackProject")

    def serviceClient(self):#
        #print(' >>> panel.9 service.Client .')

        ackpanel.minLocX.setx(33 + ackpanel.viewPortX.getx())
        ackpanel.maxLocX.setx(131 + ackpanel.viewPortX.getx())
        ackpanel.minLocY.setx(530 + ackpanel.viewPortY.getx())
        ackpanel.maxLocY.setx(577 + ackpanel.viewPortY.getx())
        ackpanel.index.setx("ackClient")
    def endClient(self):#
        #print(' >>> panel.4 end.Client .')

        ackpanel.minLocX.setx(33 + ackpanel.viewPortX.getx())
        ackpanel.maxLocX.setx(131 + ackpanel.viewPortX.getx())
        ackpanel.minLocY.setx(625 + ackpanel.viewPortY.getx())
        ackpanel.maxLocY.setx(666 + ackpanel.viewPortY.getx())
        ackpanel.index.setx("ackEnd")

    def contactServer(self):#
        #print(' >>> panel.3 contact.Server .')

        ackpanel.minLocX.setx(301 + ackpanel.viewPortX.getx())
        ackpanel.maxLocX.setx(512 + ackpanel.viewPortX.getx())
        ackpanel.minLocY.setx(230 + ackpanel.viewPortY.getx())
        ackpanel.maxLocY.setx(275 + ackpanel.viewPortY.getx())
        ackpanel.index.setx("ackContact")

panelplate = PanelPlate()
class MainLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MainLoader' property.")
mainloader = MainLoader()
class EnterLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'EnterLoader' property.")
enterloader = EnterLoader()
class ExitLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ExitLoader' property.")
exitloader = ExitLoader()
class ServerLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ServerLoader' property.")
serverloader = ServerLoader()
class MeshesRigsLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'MeshesRigsLoader' property.")
meshesrigsloader = ServerLoader()
class ArenaLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ArenaLoader' property.")
arenaloader = ArenaLoader()
class ProjectsLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ProjectsLoader' property.")
projectsloader = ProjectsLoader()
class ClientLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ClientLoader' property.")
clientloader = ClientLoader()
class EndLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'EndLoader' property.")
endloader = EndLoader()
