# !/usr/bin/env python .
# Created Sunday, August 26, 2018 .
# Blender 2.79 plld.py
# Panel Loader Section  .
# Last update : Main, Server, Enter, Exit, Meshes&Rigs, Arena, Project, Client, End  .
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
#____________________________________________
#               Panel Loader Section
#___________________________________________________________________________________________
def panelLoad():#____________________________________________________ Main Loader Section . ___________________________:(
    if mainLoader.get_n() == 1:#
        mainLoader.set_n(0)
        escMain.set_n(1)
        panelPlate.mouseEnter()
        panelPlate.mouseExit()
        def serverCall():#
            setMouse.set_n(1)
            mouseOpt.set_n(1)
        service = threading.Timer(0.5, serverCall)
        service.start()
        text.callServer()
#______________________________________________________________________________________________
    if serverLoader.get_n() == 1:# _____________________________________ Server Loader  Section .__________________________:(
        serverLoader.set_n(0)
        escOutService.set_n(1)
        userPassOpt.set_n(1)
        if classclient.single(classclient) == 1:#__________________________ ''' classclient.init_single'''__________________________:(
            classclient.init_single(0)
            self.singlePass()
            userClient.set_n(1)
            clientconnected.set_n(1)
            def serverCall():#
                self.singleAdminLogIn()
            service = threading.Timer(0.1, serverCall)
            service.start()
        if classclient.multi(classclient) == 1:#___________________________ ''' classclient.init_multi '''____________________________:(
            classclient.init_multi(0)
            self.multiPass()
            userRemote.set_n(1)
            userconnected.set_n(1)
            def serverCall():#
                self.multiAdminLogIn()
            service = threading.Timer(0.1, serverCall)
            service.start()
#____________________________________________________________________________________________
    if enterLoader.get_n() == 1:#______________________________________ Enter Loader Section . ___________________________:(
        enterLoader.set_n(0)
        def yesServer():#
            panelPlate.contactServer()
            def menu():#
                text.mainMenu()
            menuMain = threading.Timer(0.7, menu)
            menuMain.start()
        yesCall = threading.Timer(0.7, yesServer)
        yesCall.start()
        self.yesCallServer()
        def outoffService():#
            text.introOffline()
        noServer = threading.Timer(0.9, outoff.Service)
        noServer.start()
#___________________________________________________________________________________________
    if exitLoader.get_n() == 1:#________________________________________ Exit Loader Section . __________________________:(
        exitLoader.set_n(0)
        def noServer():#
            pass
            def menu():#
                text.mainMenu()
            menuMain = threading.Timer(0.7, menu)
            menuMain.start()
        noCall = threading.Timer(1.3, noServer)
        noCall.start()
        self.noCallServer()  
#____________________________________________________________________________________________________
    if meshesRigsLoader.get_n() == 1:#________________________________ Meshes Rigs Loader Section .________________________:(
        meshesRigsLoader.set_n(0)
        escSpawn.set_n(1)
        def meshesRigs():#
            self.camera360()
            mainPlates.setSpawn()
            mainPlates.setRig1()
            mainPlates.setRig2()
            mainPlates.setRig3()
        service = threading.Timer(0.7, meshesRigs)
        service.start()
        self.set_MeshesRigs()
#____________________________________________________________________________________________
    if arenaLoader.get_n() == 1:#______________________________________ Arena Loader Section .______________________________________:(
        arenaLoader.set_n(0)
        escArena.set_n(1)
        self.set_ArenaPanel()
        arena.offArena(1)
        def menuArena():#
            pass
        service = threading.Timer(0.1, menuArena)
        service.start()
#______________________________________________________________________________________________
    if projectLoader.get_n() == 1:#_____________________________________ Project Loader Section .______________________________:(
        projectLoader.set_n(0)
        escProjects.set_n(1)  
        self.set_ProjectPanel()
#____________________________________________________________________________________________
    if clientLoader.get_n() == 1:#______________________________________ Client Loader Section ._____________________________________:(
        clientLoader.set_n(0) 
        if remotePass.get_n() == 0:
            escEntry.set_n(1)
            rightClickOpt.set_n(0) 
            loaderOpt.set_n(1) 
            consoleTextOpt.set_n(1) 
            def getclientCall():#
                pass
            service = threading.Timer(0.7, getclientCall)
            service.start()
            self.clientRequest()
            cursorEntries.setEntry()
            def endclientCall():#
                cursorEntries.endEntry()
                rightClickOpt.set_n(1)
                com.setCom(0)
                consolectrl.setConsole(1)                    
            service = threading.Timer(1.4, endclientCall)
            service.start()
#_________________________________________________________________________________________
    if endLoader.get_n() == 1:#________________________________________End Loader Section .______________________________________:(
        endLoader.set_n(0)
        runserver.start(0)
        if standAlone.get_n() == 0:# 
            standAlone.set_n(1)
            registername.closeClient()
            self.clientFinalclose()
        else:#
            self.get_StandAlone()
    self.registerMouseClick()
    self.consoleLedger()
