# !/usr/bin/env python .
# Created Saturday, August 11, 2018 .
# Blender 2.79 dictclient.py
# 
# Last update :
######################
def ModuleDirectory(dir_list):#
        dir_list = []#
        for k in range(7):## Don't Forget to Update Directory key Count. . . . . . . . . . . . . . . .
            dir_list.append(dictclient.DirectoryAssembly(k))#
            ser_dirs = (('\n').join(dir_list))#
        return ser_dirs#  
################
def dict_SearchDirect():#_.........
    import LookupServiceList##
    print('> dict_SearchDirect plus dict_LookupServiceList <')#
    for k in range(8):#_____________________
        list_pack = (DirectoryFinder(k))#
        print('> SearchDirect plus LookupServiceList Keys* ',LookupServiceList.ServiceList(list_pack))#
        print(list_pack)#
################
def Lookup(key):#________________________________________________________________________________________________________
    print('> Search Direct .')#________________
    tester = dictclient.DirectoryAssembly(key)#
    return tester#
###################
def ModuleDirectory(dir_list):#
        dir_list = []#
        for k in range(7):## Don't Forget to Update Directory key Count. . . . . . . . . . . . . . . .
            dir_list.append(dictclient.DirectoryAssembly(k))#
            ser_dirs = (('\n').join(dir_list))#
        return ser_dirs#  
##############
def List_Func(key):#________________________________________________________________________________________________________
    print('> List_Func .')#
    tester = DirectoriesList.Listings(key)#.
    return tester#
