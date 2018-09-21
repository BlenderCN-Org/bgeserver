# !/usr/bin/env python .
# Created Tuesday, June 26, 2018 .
# Blender 2.79 text.py
# 
# Last update :
from bge import logic, render
import math
import ackpanel
import threading
import mouseclick
import textpanel
class TextOpt:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        self._x = None
    x = property(getx, setx, delx, " >>> 'TextOpt' property.")
textopt = TextOpt()
def InputConsole():#
    n = 0
    def func():#
        print('> InputConsole ', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def setConsole(text):#
    inputConsole.set_n(text)
def getConsole(text):#
    text = inputConsole.get_n()
    return text
inputConsole = InputConsole()

class RigPlates:
    def __init__(self):#
        self.spawnArea = 0
    def setSpawn(self):#___________________________:
        ''' >>> setSpawnMenu'''
        scene = logic.getCurrentScene()
        area = scene.objects["Camera.001"]        
        spawner = scene.objects["SpawnArea"]
        area.position = spawner.worldPosition  
        spawnArea = scene.objects["TextMenSpawnArea"]
        spawner = scene.objects["SpawnerPlateSpawnArea"]
        spawnArea.position = spawner.worldPosition
        meshStock = scene.objects["TextMenuMeshes"]
        spawner = scene.objects["SpawnerPlateMeshStock"]
        meshStock.position = spawner.worldPosition
    def setRig1(self):#___________________________:
        ''' >>> setRig1 '''
        scene = logic.getCurrentScene()
        setRig1 = scene.objects["TextRig.1"]
        spawner = scene.objects["SpawnerSpawnMenuRig1"]
        setRig1.position = spawner.worldPosition
    def setRig2(self):#___________________________:
        ''' >>> setRig2'''
        scene = logic.getCurrentScene()
        setRig2 = scene.objects["TextRig.2"]
        spawner = scene.objects["SpawnerSpawnMenuRig2"]
        setRig2.position = spawner.worldPosition
    def setRig3(self):#___________________________:
        ''' >>> setRig3'''
        scene = logic.getCurrentScene()
        setRig3 = scene.objects["TextRig.3"]
        spawner = scene.objects["SpawnerSpawnMenuRig3"]
        setRig3.position = spawner.worldPosition
rigplates = RigPlates()

class Plate:#_________________________Text Text Text Text_______________________________________________________:(

    def __init__(self):#____________________________________________:(    

        self.text = 0

    def camera180(self):
        ''' >>> set_Camera.Angle z axes 180 .'''
        Zangle = 180
        scene = logic.getCurrentScene()
        camera = scene.objects["Camera.001"]#
        xyz = camera.worldOrientation.to_euler()
        xyz[2] = math.radians(Zangle)
        camera.localOrientation = xyz.to_matrix() 

    def camera360(self):
        ''' >>> set_Camera.Angle z axes 360 .'''
        Zangle = 360
        scene = logic.getCurrentScene()
        camera = scene.objects["Camera.001"]#
        xyz = camera.worldOrientation.to_euler()
        xyz[2] = math.radians(Zangle)
        camera.localOrientation = xyz.to_matrix()
        
    def camera90(self):#____________camera90____________:(
        ''' >>> set_Camera.Angle z axes 90 .'''

        Zangle = 90
        scene = logic.getCurrentScene()
        camera = scene.objects["Camera.001"]#
        xyz = camera.worldOrientation.to_euler()
        xyz[2] = math.radians(Zangle)
        camera.localOrientation = xyz.to_matrix() 

    def mainMenu(self):#__________________________main Menu .___________________________:(

        self.camera90()
        scene = logic.getCurrentScene()
        arena = scene.objects["Camera.001"]        
        spawner = scene.objects["SpawnerMainMenu"]
        arena.position = spawner.worldPosition
        mouseclick.rtclick.setx(1)
        ackpanel.setMouse.setx(1)
        mouseclick.ltclick.setx(1)
        ackpanel.setMouse.setx(1)
        render.showMouse(1)

    def callServer(self):#____________________________callServer .___________________________:(

        ''' >>> call.Server '''
        scene = logic.getCurrentScene()
        spawnArea = scene.objects["Camera.001"]        
        spawner = scene.objects["SpawnerSND"]
        spawnArea.position = spawner.worldPosition          

    def yesCallServer(self):
        ''' >>> yes_call.Server . '''
        scene = logic.getCurrentScene()
        spawnArea = scene.objects["Camera.001"]        
        spawner = scene.objects["SpawnerYES"]
        spawnArea.position = spawner.worldPosition 

    def noCallServer(self):

        '''' >>> no_call.Server . '''
        scene = logic.getCurrentScene()
        spawnArea = scene.objects["Camera.001"]        
        spawner = scene.objects["SpawnerNo"]
        spawnArea.position = spawner.worldPosition 

    def set_Arena(self):
        ''' >>> set_ArenaPanel . '''
        def startMenu():#
            ''' start.ArenaPanel . '''
            self.arenaPanel()
            def endMenu():#
                ''' end.ArenaPanel . '''
                self.endArenaPanel()
            endMain = threading.Timer(0.7, endMenu)
            endMain.start()
        startMain = threading.Timer(0.1, startMenu)
        startMain.start()
#_________________________
    def arenaPanel(self):
        ''' >>> server.Pass . '''
        scene = logic.getCurrentScene()
        textpass = scene.objects["TextArenaInfo"]        
        spawner = scene.objects["SpawnerArenaInfo"]
        textpass.position = spawner.worldPosition 
#____________________________
    def endArenaPanel(self):
        ''' >>> end.Area . '''
        scene = logic.getCurrentScene()
        arenaPanel = scene.objects["TextArenaInfo"]        
        spawner = scene.objects["SpawnerArenaInfoReturn"]
        arenaPanel.position = spawner.worldPosition 

    def set_Project(self):
        '''' >>> set_ProjectPanel . '''
        def startMenu():#
            ''' start.ProjectPanel . '''
            self.infoProject()
            def endMenu():#
                ''' end.ProjectPanel . '''
                self.endProjectPanel()
            endMain = threading.Timer(0.7, endMenu)
            endMain.start()
        startMain = threading.Timer(0.1, startMenu)
        startMain.start()
#______________________________
    def endProjectPanel(self):
        ''' >>> end.Area . '''
        scene = logic.getCurrentScene()
        projectPanel = scene.objects["TextProjectInfo.001"]        
        spawner = scene.objects["SpawnerProjectInfoReturn"]
        projectPanel.position = spawner.worldPosition 
#__________________________
    def infoProject(self):
        self.camera90()
        scene = logic.getCurrentScene()
        place = scene.objects["TextProjectInfo.001"]        
        spawner = scene.objects["SpawnerProjectInfo"]
        place.position = spawner.worldPosition  

    def introWelcome(self):#___________________________ introWelcome .___________________________:(
        self.camera90()
        ''' >>> Camera.IntroWelcome '''
        scene = logic.getCurrentScene()
        place = scene.objects["Camera.001"]        
        spawner = scene.objects["SpawnerWelcome"]
        place.position = spawner.worldPosition
    def introOffline(self):#___________________________introOffline .___________________________:(
        scene = logic.getCurrentScene()
        place = scene.objects["Camera.001"]        
        spawner = scene.objects["SpawnerOffLine"]
        place.position = spawner.worldPosition   
    def exitClient(self):#_______________________________ exitClient ._____________:(
        def autoStartExitClient():#_______________________________ exitClient ._______:(
            self.camera90()
            scene = logic.getCurrentScene()
            place = scene.objects["Camera.001"]        
            spawner = scene.objects["SpawnExitArena"]
            place.position = spawner.worldPosition
        def autoEndExitClient():#_______________________________ exitClient .____________:(
            scene = logic.getCurrentScene()
            arena = scene.objects["Camera.001"]        
            spawner = scene.objects["SpawnerMainMenu"]
            arena.position = spawner.worldPosition
        def startMenu():#
            ''' >>> start.SpawnExitArena . '''
            autoStartExitClient()
            def endMenu():#
                ''' >>> end.SpawnExitArena . '''
                autoEndExitClient()
            endMain = threading.Timer(1.4, endMenu)
            endMain.start()
        startMain = threading.Timer(0.3, startMenu)
        startMain.start()
    def clientRequest(self):
        ''' >>> set_clientRequest '''
        scene = logic.getCurrentScene()
        textstandalone = scene.objects["TextRequest"]
        spawner = scene.objects["SpawnerServerInfo"]
        textstandalone.position = spawner.worldPosition 

    def beforeYouGo(self):#__________________________Client Off___________________________:(
        self.camera90()
        ''' >>> Contact Server '''
        scene = logic.getCurrentScene()
        spawnArea = scene.objects["Camera.001"]        
        spawner = scene.objects["BeforeYouGo"]
        spawnArea.position = spawner.worldPosition  

    def meshesRigsPanel(self):
        ''' >>> server.Pass . '''
        scene = logic.getCurrentScene()
        textpass = scene.objects["TextMeshesRigs"]        
        spawner = scene.objects["SpawnerMeshesRigs"]
        textpass.position = spawner.worldPosition 

    def set_MeshesRigs(self):
        def startMenu():#
            ''' start.Arena . '''
            def endMenu():#
                ''' end.Arena . '''
                self.endMeshesRigs()
            endMain = threading.Timer(0.3, endMenu)
            endMain.start()
        startMain = threading.Timer(1.7, startMenu)
        startMain.start()
        self.meshesRigsPanel()

    def endMeshesRigs(self):
        scene = logic.getCurrentScene()
        textpass = scene.objects["TextMeshesRigs"]        
        spawner = scene.objects["SpawnerHoldMeshesRigs"]
        textpass.position = spawner.worldPosition 

    def singleAdminLogIn(self):
        def startMenu():#
            ''' >>>                     <<< '''
            '' '>>>  start.AdminLogIn . <<< '''
            ''' >>>                     <<< '''
            self.singleServerPass()
            def endMenu():#
                ''' >>>                     <<< '''
                ''' >>>   end.AdminLogIn .  <<< '''
                ''' >>>                     <<< '''
                self.endSingleServerPass()
            endMain = threading.Timer(3.7, endMenu)
            endMain.start()
        startMain = threading.Timer(0.1, startMenu)
        startMain.start()

    def singleServerPass(self):
        ''' >>> server.Pass . '''
        scene = logic.getCurrentScene()
        textpass = scene.objects["TextSinglePass"]        
        spawner = scene.objects["SpawnerPass"]
        textpass.position = spawner.worldPosition 

    def endSingleServerPass(self):
        ''' >>>                     <<< '''
        ''' >>>   end.SinglePass .  <<< '''
        ''' >>>                     <<< '''
        scene = logic.getCurrentScene()
        obj1 = scene.objects["TextSinglePass"]
        obj1.endObject()  

    def multiAdminLogIn(self):
        def startMenu():
            ''' >>>                     <<< '''
            ''' >>>  start.AdminLogIn . <<< '''
            ''' >>>                     <<< '''
            self.multiServerPass()
            def endMenu():#
                ''' >>>                    <<< '''
                ''' >>>   end.AdminLogIn .  <<<'''
                ''' >>>                    <<< '''
                self.endMultiServerPass()
            endMain = threading.Timer(3.7, endMenu)
            endMain.start()
        startMain = threading.Timer(0.1, startMenu)
        startMain.start()

#_________________________

    def multiServerPass(self):
        ''' >>> server.Pass . '''
        scene = logic.getCurrentScene()
        textpass = scene.objects["TextMultiPass"]        
        spawner = scene.objects["SpawnerPass"]
        textpass.position = spawner.worldPosition 

#___________________________

    def endMultiServerPass(self):
        ''' >>>                     <<< '''
        ''' >>>   end.MultiPass .  <<< '''
        ''' >>>                     <<< '''
        scene = logic.getCurrentScene()
        obj1 = scene.objects["TextMultiPass"]
        obj1.endObject()  

plate = Plate()
