# !/usr/bin/env python .
# Created Tuesday, June 26, 2018 .
# Blender 2.79 text.py
# 
# Last update :
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


class Text:#_________________________Text Text Text Text_______________________________________________________:(
    def __init__(self):#____________________________________________:(    
        self.text = 0
    def camera90(self):#____________camera90____________:(
        print(' >>> set_Camera.Angle z axes 90 .')
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
        #cursorOpt.set_n(0)
        rightClickOpt.set_n(1)
        ackpanel.setMouse.setx(1)
        setMouse.set_n(1)
        mouseOpt.set_n(1)
        if panelLoaderOpt.get_n() == 0:#
            self.set_mainPanelLoader()
    def set_mainPanelLoader(self):#__________________________set_mainPanelLoader.___________________________:(
        render.showMouse(1)
        if consoleOpt.get_n() == 0:#
            panelPlate.mainHeader()
            panelPlate.serverStart()
            panelPlate.meshesRigsClient()
            panelPlate.arenaClient()
            panelPlate.projectClient()
            panelPlate.serviceClient()
            panelPlate.endClient()
    def callServer(self):#____________________________callServer .___________________________:(
        self.camera90()
        print(' >>> call.Server ')
        scene = logic.getCurrentScene()
        spawnArea = scene.objects["Camera.001"]        
        spawner = scene.objects["SpawnerSND"]
        spawnArea.position = spawner.worldPosition          
    def introWelcome(self):#___________________________ introWelcome .___________________________:(
        self.camera90()
        print(' >>> Camera.IntroWelcome ')
        scene = logic.getCurrentScene()
        place = scene.objects["Camera.001"]        
        spawner = scene.objects["SpawnerWelcome"]
        place.position = spawner.worldPosition
    def introOffline(self):#___________________________introOffline .___________________________:(
        #self.camera90()
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
            print(' >>> start.SpawnExitArena . ')
            autoStartExitClient()
            def endMenu():#
                print(' >>> end.SpawnExitArena . ')
                autoEndExitClient()
            endMain = threading.Timer(1.4, endMenu)
            endMain.start()
        startMain = threading.Timer(0.3, startMenu)
        startMain.start()

