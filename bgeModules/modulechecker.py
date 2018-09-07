# !/usr/bin/env python .
# Created Friday, June 22, 2018 .
# Blender 2.79 modulechecker.py
# 
# Last update :
print(' Module_Search *Prog Blender 2.79                ')#
print(' ------ Master Client Console Build -----')

from pathlib import Path
def cleanlist(list1):#_____________________________:(
    return str(list1).replace('"', '').replace('"', '')
file_list = []
def EndFile():#
    n = 0
    def func():#
        print('> EndFile', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def Count():#
    n = 0
    def func():#
        print('> Count', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
def Mis():#
    n = 0
    def func():#
        print(' >>> Missing files counted ,', n) # 
    def get_n():#
        return n
    def set_n(value):#
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func#_#
class TotalFiles:#_____________________________________________________________________________:(
    def __init__(self):#
        self.file = 0
    def total(self):#
        self.file  = count.get_n() + 1
        count.set_n(self.file)
class MissingFiles:#_____________________________________________________________________________:(
    def __init__(self):#
        self.file = 0
    def decount(self):#
        self.file  = mis.get_n() + 1
        mis.set_n(self.file)
missingFiles = MissingFiles()
totalFiles = TotalFiles()
endFile = EndFile()
count = Count()
mis = Mis()
client_infile = open("C:/Python34/Blender_Modules/BGEClientUpdate.txt ")
if client_infile:#
    infile = open('BGEClientUpdate.txt', 'r')
    for f in infile :#
        file_list.append(f)
main_root = "C:/Program Files/Blender Foundation/Blender/"
for f in file_list:#
    if f == '\n':#
        break
    totalFiles.total()
    count()
    cleanlist(f)
    file =cleanlist(f).rstrip('\n')
    my_file = Path(main_root + file)
    if my_file.is_file():#
        infile = open(file, 'r')
        firstLine = infile.readline()
        secondLine = infile.readline()
        thirdLine = infile.readline()
        forthLine = infile.readline()
        fifthLine = infile.readline() 
        print(secondLine, thirdLine, fifthLine)
    else:#
        missingFiles.decount()
        mis()
        print(' >>> missing file . ', f)#
        print(' ')
total = len(file_list)
total_miss = mis.get_n()
print(' >>> Total of ', total, ', BGE Client Console Modules . <<< ')#
print(' >>> Missing ', total_miss, ', BGE Client Console Modules . <<< ')#
