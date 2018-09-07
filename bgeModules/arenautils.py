# !/usr/bin/env python .
# Created Sunday, August 26, 2018 .
# Blender 2.79 arenautils.py
# 
# Last update :  
###########################################
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
#########################
from bge import logic
import math
import objconfig


def dropOffRig():#________________________________________________:(
    introResetRig() 
    def selfdropOff():#
        #self.camera360()
        #mainPlates.setSpawn()
        print(' >>> dropOffRig ')           
    dropOff = threading.Timer(0.7, selfdropOff)
    dropOff.start()

def rig1PolygonFactoryDelete():#____________________________________________________________:(

    scene = logic.getCurrentScene()
    obj1 = scene.objects["Suzanne"]
    obj1.endObject()

def deParentPlayerCamera():#_____________________________:(
    print(' >>>                      <<< ')  
    print(' >>> deParent Player Camera <<< ')
    print(' >>>                      <<< ')   
    scene = logic.getCurrentScene()
    objList = scene.objects
    camera = objList["CameraRightView"]
    camera.removeParent()
    if objconfig.getmountcam(objconfig) == 1:#
        objconfig.setmountcam(0)
        print(' >>> set_Camera.Angle z axes 180 .')
        Zangle = 180
        scene = logic.getCurrentScene()
        camera = scene.objects["CameraRightView"]#
        xyz = camera.worldOrientation.to_euler()
        xyz[2] = math.radians(Zangle)
        camera.localOrientation = xyz.to_matrix() 

def endRig1():#______________________________________________________________________________:(
    #rig1Control.set_n(0)
    #objconfig.setcontrols(0)
    scene = logic.getCurrentScene()
    obj1 = scene.objects["Rig1"]
    obj1.endObject()  
#
def resetRig1():#_________________________________________________________________:(
    resetRig1.set_n(0)
    mesh1Factory.set_n(1)
    print(' >>> rig1.Reset ')
    scene = logic.getCurrentScene()
    spawner = scene.objects["SpawnerRig1"]
    rig1 = scene.addObject("Rig1", spawner)
    spawner = scene.objects["SuzannesPoint"]
    mesh1 = scene.addObject("Suzanne", spawner)
