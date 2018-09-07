# !/usr/bin/env python .
# Created Thursday, August 16, 2018 .
# Blender 2.79 camerasetup.py
# 
# Last update :
    def setCameraLevels(self):#________________________________________________________________:(
        if tabCon.get_n() == 1:#
            level1Camera.set_n(1)
            print(' >>> level1Camera .')
        if tabCon.get_n() == 2:#
            level2Camera.set_n(1)
            print(' >>> level2Camera .')
        if tabCon.get_n() == 3:#
            level3Camera.set_n(1)
            print(' >>> level3Camera .')
        if tabCon.get_n() == 4:#
            level4Camera.set_n(1)
            print(' >>> leve4Camera .')
#
    def frontLevel1View(self):#________________________________________________________________:(
        self.adjustCameraAngle()
        self.setCameraAngle()
        print(' >>> set_camera.Level 1 toggle .')
        scene = logic.getCurrentScene()
        camera = scene.objects["Camera.001"]      
        spawner = scene.objects["FrontCameraLevel1"]
        xyz = camera.worldOrientation.to_euler()
        xyz[2] = math.radians(360)
        camera.localOrientation = xyz.to_matrix()
        camera.position = spawner.worldPosition
#
    def frontLevel2View(self):#________________________________________________________________:(
        self.adjustCameraAngle()
        self.setCameraAngle()
        print(' >>> set_camera.Level 2 toggle .')
        scene = logic.getCurrentScene()
        camera = scene.objects["Camera.001"]      
        spawner = scene.objects["FrontCameraLevel2"]
        xyz = camera.worldOrientation.to_euler()
        xyz[2] = math.radians(360)
        camera.localOrientation = xyz.to_matrix()
        camera.position = spawner.worldPosition
#
    def frontLevel3View(self):#________________________________________________________________:(
        self.adjustCameraAngle()
        self.setCameraAngle()
        print(' >>> set_camera.Level 3 toggle .')
        scene = logic.getCurrentScene()
        camera = scene.objects["Camera.001"]      
        spawner = scene.objects["FrontCameraLevel3"]
        xyz = camera.worldOrientation.to_euler()
        xyz[2] = math.radians(360)
        camera.localOrientation = xyz.to_matrix()
        camera.position = spawner.worldPosition
#
    def frontLevel4View(self):#________________________________________________________________:(
        self.adjustCameraAngle()
        self.setCameraAngle()
        print(' >>> set_camera.Level 4 toggle .')
        scene = logic.getCurrentScene()
        camera = scene.objects["Camera.001"]      
        spawner = scene.objects["FrontCameraLevel4"]
        xyz = camera.worldOrientation.to_euler()
        xyz[2] = math.radians(360)
        camera.localOrientation = xyz.to_matrix()
        camera.position = spawner.worldPosition
#
    def cameraDirector(self):#___________________________________________________________:(
        anchor1Cam.set_n(0)
        anchor2Cam.set_n(0)
        anchor3Cam.set_n(0)
        anchor4Cam.set_n(0)    
#
    def setCameraAngle(self):#___________________________________________________________:(
        print(' >>> set_Camera.Angle .')
        angle = adjustAngleCam.get_n()
        scene = logic.getCurrentScene()
        camera = scene.objects["Camera.001"]#
        xyz = camera.worldOrientation.to_euler()
        xyz[0] = math.radians(angle)
        camera.localOrientation = xyz.to_matrix()
#
    def resetCameraAngle(self):##_________________________________________________________________:(
        print(' >>> set_Camera.Angle .')
        angle = 90
        scene = logic.getCurrentScene()
        camera = scene.objects["Camera.001"]#
        xyz = camera.worldOrientation.to_euler()
        xyz[0] = math.radians(angle)
        camera.localOrientation = xyz.to_matrix()        
#
    def resetCameraXAngle(self):##_________________________________________________________________:(
        camTrack.set_n(0)
        print(' >>> reset_Camera.ZAngle .')
        angle = adjustAngleCam.get_n() 
        scene = logic.getCurrentScene()
        camera = scene.objects["Camera.001"]#
        xyz = camera.worldOrientation.to_euler()
        xyz[0] = math.radians(angle)
        camera.localOrientation = xyz.to_matrix()  
#
    def adjustCameraAngle(self):#______________________________________________________________:(
        if tabCon.get_n() == 1:#
            adjustAngleCam.set_n(77.0)
        if tabCon.get_n() == 2:#
            adjustAngleCam.set_n(55.0)
        if tabCon.get_n() == 3:#
            adjustAngleCam.set_n(40.0)
        if tabCon.get_n() == 4:#
            adjustAngleCam.set_n(77.0) 
        self.resetCameraXAngle()
#
    def nextCameraLevel(self):#________________________________________________________________________:(
        print(' >>> set_nextCameraLevel.Angle .')
        scene = logic.getCurrentScene()
        camera = scene.objects["Camera.001"]      
        spawner = scene.objects["FrontView"]
        xyz = camera.worldOrientation.to_euler()
        xyz[2] = math.radians(360)
        camera.localOrientation = xyz.to_matrix()
        camera.position = spawner.worldPosition    
#
    def upDateAnchorTag(self):#___________________________________________________________________:(
        scene = logic.getCurrentScene()
        if current1Anchor.get_n() == 1:#
            current1Anchor.set_n(0)
            camera_tag = scene.objects["CameraFrontTAG"]
            camera_tag.endObject() 
        if current2Anchor.get_n() == 1:#
            current2Anchor.set_n(0)
            camera_tag = scene.objects["CameraBackTAG"]
            camera_tag.endObject() 
        if current3Anchor.get_n() == 1:#
            current3Anchor.set_n(0)
            camera_tag = scene.objects["CameraRightTAG"]
            camera_tag.endObject() 
        if current4Anchor.get_n() == 1:#
            current4Anchor.set_n(0)
            camera_tag = scene.objects["CameraLeftTAG"]
            camera_tag.endObject() 
#
#    def frontView(self):#________________________________________________________________:(
#        self.adjustCameraAngle()
#        camArena.set_n(0)
#        self.upDateAnchorTag()
#        anchor1Cam.set_n(1)
#        anchor2Cam.set_n(0)
#        anchor3Cam.set_n(0)
#        anchor4Cam.set_n(0)
#        self.resetCameraAngle()
#        print(' >>> front.View .')
#        scene = logic.getCurrentScene()
#        camera = scene.objects["Camera.001"]      
#        spawner = scene.objects["FrontView"]
#        xyz = camera.worldOrientation.to_euler()
#        xyz[2] = math.radians(360)
#        camera.localOrientation = xyz.to_matrix()
#        camera.position = spawner.worldPosition
#        self.upDateAnchorTag()
#        cameraAnchor = scene.objects["MainCameraAnchor"]
#        view_tag = scene.addObject("CameraFrontTAG", cameraAnchor)
#        current1Anchor.set_n(1)
#
#    def backView(self):#________________________________________________________________:(
#        camArena.set_n(0)
#        self.upDateAnchorTag()
#        anchor1Cam.set_n(0)
#        anchor2Cam.set_n(1)
#        anchor3Cam.set_n(0)
#        anchor4Cam.set_n(0)
#        self.resetCameraAngle()
#        print(' >>> back.View .')
#        scene = logic.getCurrentScene()
#        camera = scene.objects["Camera.001"]      
#        spawner = scene.objects["BackView"]
#        xyz = camera.worldOrientation.to_euler()
#        xyz[2] = math.radians(180)
#        camera.localOrientation = xyz.to_matrix()
#        camera.position = spawner.worldPosition
#        cameraAnchor = scene.objects["MainCameraAnchor"]
#        view_tag = scene.addObject("CameraBackTAG", cameraAnchor)
#        current2Anchor.set_n(1)
#
    def rightView(self):#________________________________________________________________:(
        camArena.set_n(0)
        self.upDateAnchorTag()
        anchor1Cam.set_n(0)
        anchor2Cam.set_n(0)
        anchor3Cam.set_n(1)
        anchor4Cam.set_n(0)
        self.resetCameraAngle()
        print(' >>> right.View .')
        scene = logic.getCurrentScene()
        camera = scene.objects["Camera.001"]      
        spawner = scene.objects["RightView"]
        xyz = camera.worldOrientation.to_euler()
        xyz[2] = math.radians(90)
        camera.localOrientation = xyz.to_matrix()
        camera.position = spawner.worldPosition
        cameraAnchor = scene.objects["MainCameraAnchor"]
        view_tag = scene.addObject("CameraRightTAG", cameraAnchor)
        current3Anchor.set_n(1)
#
    def leftView(self):#________________________________________________________________:(
        camArena.set_n(0)
        self.upDateAnchorTag()
        anchor1Cam.set_n(0)
        anchor2Cam.set_n(0)
        anchor3Cam.set_n(0)
        anchor4Cam.set_n(1)
        self.resetCameraAngle()
        print(' >>> left.View .')
        scene = logic.getCurrentScene()
        camera = scene.objects["Camera.001"]      
        spawner = scene.objects["LeftView"]
        xyz = camera.worldOrientation.to_euler()
        xyz[2] = math.radians(270)
        camera.localOrientation = xyz.to_matrix()
        camera.position = spawner.worldPosition
        cameraAnchor = scene.objects["MainCameraAnchor"]
        view_tag = scene.addObject("CameraLeftTAG", cameraAnchor)
        current4Anchor.set_n(1)
#
    def shiftScope(self):#_____________________________________________________________________________:(
        scene = logic.getCurrentScene()
        objList = scene.objects
        camera = objList["Camera.001"]
        camatrix = camera.projection_matrix
        shitfy = -0.625
        camatrix[1][2] = 2*shitfy
        camera.projection_matrix = camatrix           
#
    def cameraCenterShift(self):#__________________________________________________________________:(
        scene = logic.getCurrentScene()
        objList = scene.objects
        camera = objList["Camera.001"]
        camatrix = camera.projection_matrix
        shiftx = 0.0
        shitfy = 0.0
        camatrix[0][2] = shiftx
        camatrix[1][2] = shitfy
        camera.projection_matrix = camatrix   
#
    def cameraFocus(self):#________________________________________________________________:(
        print(' >>> set_camera.Zoom .')
        scene = logic.getCurrentScene()
        scene.objects["Camera.001"].lens = 35.00
#
    def cameraZoom(self):#________________________________________________________________:(
        print(' >>> set_camera.Zoom .')
        scene = logic.getCurrentScene()
        scene.objects["Camera.001"].lens = 166.50
