# !/usr/bin/env python .
# Created Monday, August 13, 2018 .
# Blender 2.79 userfunctions.py
# Library for New Created Functions
# Last update :
import configdeltas
import iduser
from bge import logic
import math
import objfunc
import batglob
import scheduleclient
import initobjs
import polyfactory
import cltrequest
import tracker
import meshbuild
def loadfunction():#
    func_input = iduser.initUserEnd(iduser)    
    if configdeltas.loadlogin(configdeltas) == 1:#
        configdeltas.deletelogin(0)

        if func_input == 'login':#
            data = {'house':'5', 'name': 'Login ', 'town': 'Stephenville'}# 
            return data# 
            
        if func_input == 'blake':#
            data = {'house':'710', 'name': 'l3lak3', 'town': 'Stephenville'}# 
            return data# 

    if configdeltas.loadserver(configdeltas) == 1:#
        configdeltas.deleteserver(0)

        if func_input == 'active':#
            data = {'house':'5', 'name': 'Server Active ', 'town': 'Stephenville'}# 
            return data#

    if configdeltas.loadschedules(configdeltas) == 1:#
        configdeltas.deleteschedules(0)

        if func_input == 'sch0':#
            data = {'house':'5', 'name': 'Schedules', 'town': 'Stephenville'}# dict_tester
            return data# 

        if func_input == 'sch1':#
            data = {'house':'5', 'name': 'Schedule 1', 'town': 'Stephenville'}# 
            scheduleclient.schedrig.setx(1)
            scheduleclient.schedmesh.setx(1)
            scheduleclient.schedcam.setx(1)
            scheduleclient.schedcont.setx(1)
            initobjs.main.setx(1)
            return data# 

        if func_input == 'sch2':#
            data = {'house':'5', 'name': 'Tracker ON', 'town': 'Stephenville'}# dict_tester
            tracker.main.setx(1)
            return data# 

        if func_input == 'sch3':#
            data = {'house':'5', 'name': 'Tracker OFF', 'town': 'Stephenville'}# dict_tester
            tracker.main.delx()
            return data# 

        if func_input == 'sch4':#
            data = {'house':'5', 'name': 'pacman.setJaws', 'town': 'Stephenville'}# dict_tester
            meshbuild.pacman.closeJaws()
            return data# 

        if func_input == 'sch5':#
            data = {'house':'5', 'name': 'moveJaws', 'town': 'Stephenville'}# dict_tester
            meshbuild.pacman.moveJaws()
            return data# 

    if configdeltas.loadassembly(configdeltas) == 1:#
        configdeltas.deleteassembly(0)

        if func_input == 'gstar':#
            data = {'house':'5', 'name': 'Assembly gstar  ', 'town': 'Stephenville'}# dict_testers
            return data# 

        if func_input == 'rig':#
            data = {'house':'5', 'name': 'Assembly Rig', 'town': 'Stephenville'}# 
            objfunc.setrig(1)
            return data# 

        if func_input == 'mesh':#
            data = {'house':'5', 'name': 'Assembly Mesh', 'town': 'Stephenville'}# 
            objfunc.setmesh(1)
            return data# 

        if func_input == 'cam':#
            data = {'house':'5', 'name': 'Assembly Camera', 'town': 'Stephenville'}# 
            objfunc.setcam(1)
            return data# 

        if func_input == 'controls':#
            data = {'house':'5', 'name': 'Assembly Controls', 'town': 'Stephenville'}# dict_testers
            objfunc.setkeyboard(1)
            return data# 

    if configdeltas.loadfunctions(configdeltas) == 1:#
        configdeltas.deletefunctions(0)
        if func_input == 'func0':#
            data = {'house':'5', 'name': 'func0 ', 'town': 'Stephenville'}# dict_testers
            polyfactory.main.setx(2)
            return data# 

        if func_input == 'reload':#
            data = {'house':'5', 'name': 'reload ', 'town': 'Stephenville'}#
            polyfactory.main.setx(1)
            return data# 

        if func_input == 'faccess':#
            data = {'house':'5', 'name': 'faccess ', 'town': 'Stephenville'}# 
            batglob.setaccess(1)
            return data# 

        if func_input == 'fload':#
            data = {'house':'5', 'name': 'fload ', 'town': 'Stephenville'}# 
            batglob.setload(1)
            return data# 

        if func_input == 'fsave':#
            data = {'house':'5', 'name': 'fsave ', 'town': 'Stephenville'}# 
            batglob.setsave(1)
            return data# 

    if configdeltas.loadviewport(configdeltas) == 1:#
        configdeltas.deleteviewport(0)
        if func_input == 'aux':#
            data = {'house':'5', 'name': 'Viewport aux ', 'town': 'Stephenville'}# 
            return data# 

        if func_input == 'front':#
            data = {'house':'5', 'name': 'Front Arena', 'town': 'Stephenville'}# 
            scene = logic.getCurrentScene()
            camera = scene.objects["CameraLeftView"]      
            spawner = scene.objects["FrontView.001"]
            xyz = camera.worldOrientation.to_euler()
            xyz[2] = math.radians(360)
            camera.localOrientation = xyz.to_matrix()
            camera.position = spawner.worldPosition
            return data# 

        if func_input == 'back':#
            data = {'house':'5', 'name': 'Back Arena', 'town': 'Stephenville'}# 
            scene = logic.getCurrentScene()
            camera = scene.objects["CameraLeftView"]      
            spawner = scene.objects["BackCameraLevel2"]
            xyz = camera.worldOrientation.to_euler()
            xyz[2] = math.radians(180)
            camera.localOrientation = xyz.to_matrix()
            camera.position = spawner.worldPosition
            return data# 

    if configdeltas.loadmouse(configdeltas) == 1:#
        configdeltas.deletemouse(0)
        if mouse_input == 'mload':#
            data = {'house':'5', 'name': 'mload ', 'town': 'Stephenville'}# 
            return data# 

    if configdeltas.loadrequest(configdeltas) == 1:#
        configdeltas.deleterequest(0)
        deltas = cltrequest.loadfunction()
        if func_input in str(deltas):#
            data = {'house':'5', 'name': (func_input), 'town': 'Stephenville'}# 
            return data# 

    else:#
        data = {'house':'empty', 'name': 'empty', 'town': 'empty'}# 
        return data#   
