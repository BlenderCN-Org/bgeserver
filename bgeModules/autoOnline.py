# !/usr/bin/env python .
# Created Friday, June 22, 2018 .
# Blender 2.79 autoOnline.py
# 
# Last update :
from bge import logic
def autoOnline():#
    scene = logic.getCurrentScene()
    autoOnline = scene.objects["Camera.001"]        
    spawner = scene.objects["SpawnerOnline"]
    autoOnline.position = spawner.worldPosition 
def singlePass():#
    scene = logic.getCurrentScene()
    textSingle = scene.objects["TextSingle"]        
    single = scene.objects["SpawnerSinglePass"]
    textSingle.position = single.worldPosition 
def multiPass():#
    scene = logic.getCurrentScene()
    textMult = scene.objects["TextMulti"]        
    multi = scene.objects["SpawnerMultiPass"]
    textMult.position = multi.worldPosition #
