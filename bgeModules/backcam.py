# !/usr/bin/env python .
# Created Thursday, August 16, 2018 .
# Blender 2.79 backcam.py
# 
# Last update :
from bge import logic
import math
print(' >>> back.View .')
scene = logic.getCurrentScene()
camera = scene.objects["CameraLeftView"]      
spawner = scene.objects["BackCameraLevel2"]
xyz = camera.worldOrientation.to_euler()
xyz[2] = math.radians(180)
camera.localOrientation = xyz.to_matrix()
camera.position = spawner.worldPosition
