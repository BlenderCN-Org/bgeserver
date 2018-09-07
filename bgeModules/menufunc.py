# !/usr/bin/env python .
# Created Tuesday, August 21, 2018 .
# Blender 2.79 menufunc.py
# 
# Last update :
#
import iduser
import configdeltas 
import mmenu
import initmenu
import idmenu
import dictmenu
import configmenu
import batmenu
import libmenu
def loadfunction():#
    func_input = iduser.initUserEnd(iduser)
    if configdeltas.loadRig(configdeltas) == 1:#
        configdeltas.deleteRig(0)
#
        if func_input == '_mm_':#
            data = {'house':'5', 'name': 'Main menu', 'town': 'Stephenville'}
            mmenu.mainmenu.setx(1)
            return data#
#
        if func_input == '_init_':#
            data = {'house':'5', 'name': 'Init main', 'town': 'Stephenville'}
            initmenu.initmain.setx(1)
            return data#
#
        if func_input == '_id_':#
            data = {'house':'5', 'name': 'Id main', 'town': 'Stephenville'}
            idmenu.idmain.setx(1)
            return data#
#
        if func_input == '_dict_':#
            data = {'house':'5', 'name': 'Dict main', 'town': 'Stephenville'} 
            dictmenu.dictmain.setx(1)   
            return data#
#
        if func_input == '_config_':#
            data = {'house':'5', 'name': 'Config main', 'town': 'Stephenville'} 
            configmenu.configmain.setx(1)
            return data#
#
        if func_input == '_bat_':#
            data = {'house':'5', 'name': 'Bat main', 'town': 'Stephenville'} 
            batmenu.batmain.setx(1)
            return data#
#
        if func_input == '_lib_':#
            data = {'house':'5', 'name': 'Lib main', 'town': 'Stephenville'} 
            libmenu.libmain.setx(1)
            return data#
#
    else:#
        data = {'house':'empty', 'name': 'empty', 'town': 'empty'} 
        return data#           


        
