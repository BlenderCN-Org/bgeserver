# !/usr/bin/env python .
# Created Thursday, August 16, 2018 .
# Blender 2.79 frontcam.py
# 
# Last update :
from bge import logic
import math
print(' >>> front.View .')
scene = logic.getCurrentScene()
camera = scene.objects["CameraLeftView"]      
spawner = scene.objects["FrontView.001"]
xyz = camera.worldOrientation.to_euler()
xyz[2] = math.radians(360)
camera.localOrientation = xyz.to_matrix()
camera.position = spawner.worldPosition
