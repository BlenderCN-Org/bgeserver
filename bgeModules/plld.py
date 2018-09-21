# !/usr/bin/env python .
# Created Sunday, August 26, 2018 .
# Blender 2.79 plld.py
# Panel Loader Section  .
# Last update : Main, Server, Enter, Exit, Meshes&Rigs, Arena, Project, Client, End  .
###########################################
from bge import logic, render
import math
import ackpanel
import config
import threading
import mouseclick
import text
import filesys
import classclient
import ctrl
import com
import consolectrl
import registername
import runserver
import idclient
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
#____________________________________________
#               Panel Loader Section
#
# Main ' ' . 
# Server  ' ' . 
# Enter  ' ' .
# Exit  ' ' .
# Meshes Rigs  ' ' .
# Arena  ' ' .
# Project  ' ' .
# Client  ' ' .
# End  ' ' .
#
class CursorEntries:#
    def __init__(self):#
        self.entries = 0
    def setEntry(self):#___________________________:
        ''' >>> set.ConsoleEntry'''
        scene = logic.getCurrentScene()
        setText = scene.objects["CursorRequestPlaceHolder"]        
        spawner = scene.objects["SpawnerMainEntries"]
        setText.position = spawner.worldPosition
    def endEntry(self):#___________________________:
        ''' >>> end.ConsoleEntry'''
        scene = logic.getCurrentScene()
        endText = scene.objects["CursorRequestPlaceHolder"]        
        spawner = scene.objects["SpawnerHolderForEntries"]
        endText.position = spawner.worldPosition 
        endText = scene.objects["TextRequest"]
        spawner = scene.objects["SpawnerHolderRequest"]
        endText.position = spawner.worldPosition
cursorEntries = CursorEntries()
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
#________________________
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
#________________________
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
#________________________
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
#________________________
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
meshesrigsloader = MeshesRigsLoader()
#________________________
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
#________________________
class ProjectLoader:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'ProjectLoader' property.")
projectloader = ProjectLoader()
#________________________
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
#________________________
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
def CloseDown():#
    n = 0
    def func():#
        print('> CloseDown', n) #  
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
closeDown = CloseDown()
def EndOnce():#
    n = 0
    def func():#
        print('> EndOnce', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
endOnce = EndOnce()
#____________________________________________
#               Panel Loader Section
#___________________________________________________________________________________________
def mainPanel():#____________________________________________________ Main Loader Section . ___________________________:(
    mainloader.setx(1)
    text.plate.callServer()
    render.showMouse(1)
#______________________________________________________________________________________________
def ackEnter():#_
    enterloader.setx(1)
    def yesServer():#
        text.plate.callServer()
        filesys.startserver.getx()
    yesCall = threading.Timer(0.7, yesServer)
    yesCall.start()
    mouseclick.rtclick.setx(1)
    render.showMouse(0)
    text.plate.yesCallServer()

    def mainService():#
        text.plate.mainMenu()
        render.showMouse(1)
        render.showMouse(1)
    noServer = threading.Timer(0.9, mainService)
    noServer.start()
#______________________________________________________________________________________________
def ackExit():#_
    exitloader.setx(1)

    def noServer():#
        text.plate.noCallServer()

    noCall = threading.Timer(0.7, noServer)
    noCall.start()
    mouseclick.rtclick.setx(1)
    render.showMouse(0)

    def autoffService():#
        text.plate.introOffline()
    noServer = threading.Timer(0.8, autoffService)
    noServer.start()

    def mainService():#
        text.plate.mainMenu()
        render.showMouse(1)
    noServer = threading.Timer(0.9, mainService)
    noServer.start()
#______________________________________________________________________________________________
def ackServer():#_
    serverloader.setx(1)
    if classclient.single(classclient) == 1:#
        classclient.init_single(0)

        mouseclick.rtclick.setx(1)
        ''' >>> classclient.init_single'''
        #ctrl.userclient.setx(1)
        #ctrl.clientconnected.setx(1)

        def serverCall():#
            text.plate.singleAdminLogIn()
        service = threading.Timer(0.1, serverCall)
        service.start()
  
    if classclient.multi(classclient) == 1:#
        classclient.init_multi(0)

        mouseclick.rtclick.setx(1)

        ''' >>> classclient.init_multi '''
        #ctrl.userremote.setx(1)
        #ctrl.userconnected.setx(1)

        def serverCall():#
            text.plate.multiAdminLogIn()
        service = threading.Timer(0.1, serverCall)
        service.start()

#______________________________________________________________________________________________
def ackMeshesRigs():#_
    meshesrigsloader.setx(1)

    text.plate.camera360()
    text.rigplates.setSpawn()
    text.rigplates.setRig1()
    text.rigplates.setRig2()
    text.rigplates.setRig3()

    mouseclick.rtclick.setx(1)
    render.showMouse(0)
    text.plate.set_MeshesRigs()

#______________________________________________________________________________________________
def ackArena():#_
    arenaloader.setx(1)
    mouseclick.rtclick.setx(1)
    render.showMouse(0)
    text.plate.set_Arena()
#______________________________________________________________________________________________
def ackProject():#_
    projectloader.setx(1)
    mouseclick.rtclick.setx(1)
    render.showMouse(0)
    text.plate.set_Project()
#______________________________________________________________________________________________
def ackClient():#_
    clientloader.setx(1)
    mouseclick.rtclick.setx(0)
    
    def getclientCall():#
        render.showMouse(1)
    service = threading.Timer(0.7, getclientCall)
    service.start()
    text.plate.clientRequest()
    cursorEntries.setEntry()
    def endclientCall():#
        cursorEntries.endEntry()
        com.setCom(0)
        consolectrl.setConsole(1)                    
    service = threading.Timer(0.9, endclientCall)
    service.start()
    mouseclick.rtclick.setx(1)
#______________________________________________________________________________________________
def ackEnd():#_
    endloader.setx(1)
    runserver.start(0)
    render.showMouse(0)
    mouseclick.rtclick.setx(0)
    registername.closeClient()
    clientFinalclose()
#______________________________________________________________________________________________
def ackContact():#_
    pass
#_____________________
def clientFinalclose():

    if idclient.getLogOff(idclient) == 1:#
        idclient.setLogOff(0)

        ctrl.clientconnected.setx(0)
        config.closeClient(1)
        ctrl.userconnected.setx(0)
        config.closeRemote(1)
        ''' >>> Client Final Close ! <<< '''

        def serverExit():#
            text.plate.exitClient()        
        service = threading.Timer(3.7, serverExit)
        service.start()
        closeDown.set_n(1)
        def sleepExit():#
            ''' >>> * Comeback Soon ! <<< '''
        service = threading.Timer(2.7, sleepExit)
        service.start()

        def selfQuit():#
            ''' User/Client Ended Arena '''
            if endOnce.get_n() == 1:#
                endOnce.set_n(0)
                ''' >>> Goodbye Client User .<<< '''

                def sleepExit():#
                    ''' >>> Client Shutdown Finished ! <<< '''
                service = threading.Timer(6.4, sleepExit)
                service.start()

    if closeDown.get_n() == 1:#
        ''' Break the Satillites Server Communications Port Bind ! '''
        endOnce.set_n(1)
        close1Quit = threading.Timer(3.0, selfQuit)
        close1Quit.start()

        def sleepExit():#
            ''' >>> Comeback Soon ! <<< '''
            logic.endGame()
        service = threading.Timer(7.0, sleepExit)
        service.start()

        render.showMouse(0)
        text.plate.beforeYouGo()
