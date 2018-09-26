# !/usr/bin/env python .
# Created Friday September 21, 2018 .
# Blender 2.79 meshbuild.py
# 
# Last update :
from bge import logic
import math
import config
import threading
def JawTopOpen():#
    n = 0
    def func():#
        pass
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
jawtopopen = JawTopOpen()

def JawBottomOpen():#
    n = 0
    def func():#
        pass
    def get_n():#
        return n
    def set_n(value):
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
jawbottomopen = JawBottomOpen()

class PacMan:

    def __init__(self):

        self.pac = []
        self.scene = logic.getCurrentScene()

    def openJaws(self):#____________Wednesday May 23 2018 Pac Man Moves Jaws ._____:(

        def setTopJawAngle():

            jawtopopen.set_n(238) 

            angle = jawtopopen.get_n()
            jawTop = self.scene.objects["TopJaw"]
            xyz = jawTop.localOrientation.to_euler()
            xyz[0] = math.radians(angle)
            jawTop.localOrientation = xyz.to_matrix() 
        setTopJawAngle()

        def setBottomJawAngle():

            jawbottomopen.set_n(118)

            angle = jawbottomopen.get_n()
            jawBottom = self.scene.objects["BottomJaw"]
            xyz = jawBottom.localOrientation.to_euler()
            xyz[0] = math.radians(angle)
            jawBottom.localOrientation = xyz.to_matrix()
        setBottomJawAngle()

    def closeJaws(self):#____________Wednesday May 23 2018 Pac Man Moves Jaws ._____:(

        def setTopJawAngle():

            jawtopopen.set_n(308) 

            angle = jawtopopen.get_n()
            jawTop = self.scene.objects["TopJaw"]
            xyz = jawTop.localOrientation.to_euler()
            xyz[0] = math.radians(angle)
            jawTop.localOrientation = xyz.to_matrix() 
        setTopJawAngle()
     
        def setBottomJawAngle():

            jawbottomopen.set_n(49)

            angle = jawbottomopen.get_n()
            jawBottom = self.scene.objects["BottomJaw"]
            xyz = jawBottom.localOrientation.to_euler()
            xyz[0] = math.radians(angle)
            jawBottom.localOrientation = xyz.to_matrix()
        setBottomJawAngle()

    def pacmanEater(self):#____________May 20 Sunday 2018______* The Eater Build . ________________:(

        def topJaw():#

            angle = jawtopopen.get_n()

            jawTop = self.scene.objects["TopJaw"]
            xyz = jawTop.localOrientation.to_euler()
            xyz[0] = math.radians(angle)
            jawTop.localOrientation = xyz.to_matrix()
        topJaw()

        def bottomJaw():

            angle = jawbottomopen.get_n()

            jawBottom = self.scene.objects["BottomJaw"]
            xyz = jawBottom.localOrientation.to_euler()
            xyz[0] = math.radians(angle)
            jawBottom.localOrientation = xyz.to_matrix()
        bottomJaw()



    def updatePacEater(self):#_____________________________________:(
        ''' get the the worldOrientation of Meshbody ["MeshBuild"]'''

        avatar = self.scene.objects["MeshBuild"]
        xyz = avatar.localOrientation.to_euler()
        xyz = math.degrees(xyz[2])
        meshBuildPostion.set_n(xyz)
        meshBuildPostion()

    def setJaws(self):

        topjaw = self.scene.objects["TopJaw"]
        angle = jawtopopen.get_n()
        xyz = topjaw.localOrientation.to_euler()
        xyz[2] = math.radians(angle)
        topjaw.localOrientation = xyz.to_matrix()

        bottomjaw = self.scene.objects["BottomJaw"]
        angle = jawbottomopen.get_n()
        xyz = bottomjaw.localOrientation.to_euler()
        xyz[2] = math.radians(angle)
        bottomjaw.localOrientation = xyz.to_matrix()    

pacman = PacMan()
