#!/usr/bin/env python
# Created Sept,9,2017
print(' Module_Search *Prog Threading Server 101* v.9,9,17 * * * * * * * * * * * * * * * * * *')####################
print(' ----------------------------------------------------')
######################
from pathlib import Path
############################
my_file = Path("c:/Python34/mymodule.py")
if my_file.is_file():
    infile = open('c:/Python34/mymodule.py', 'r')
    firstLine = infile.readline()
    secondLine = infile.readline()
    print ('    Mymodule',secondLine)
else:
    print(' missing file Mymodule')
###################
my_file = Path("c:/Python34/MainReplies.py")
if my_file.is_file():
    infile = open('c:/Python34/MainReplies.py', 'r')
    firstLine = infile.readline()
    secondLine = infile.readline()
    print ('    MainReplies',secondLine)
else:
    print(' missing file MainReplies')
######################
my_file = Path("c:/Python34/MainRequest.py")
if my_file.is_file():
    infile = open('c:/Python34/MainRequest.py', 'r')
    firstLine = infile.readline()
    secondLine = infile.readline()
    print ('    MainRequest',secondLine)
else:
    print(' missing file MainRequest')
######################
my_file = Path("c:/Python34/ServiceDirectory.py")
if my_file.is_file():
    infile = open('c:/Python34/ServiceDirectory.py', 'r')
    firstLine = infile.readline()
    secondLine = infile.readline()
    print ('    ServiceDirectory',secondLine)
else:
    print(' missing file ServiceDirectory')
######################     
my_file = Path("c:/Python34/Identifiers.py")
if my_file.is_file():
    infile = open('c:/Python34/Identifiers.py', 'r')
    firstLine = infile.readline()
    secondLine = infile.readline()
    print ('    Identifiers',secondLine)
else:
    print(' missing file Identifiers')
###################### 
my_file = Path("c:/Python34/SearchDirect.py")
if my_file.is_file():
    infile = open('c:/Python34/SearchDirect.py', 'r')
    firstLine = infile.readline()
    secondLine = infile.readline()
    print ('    SearchDirect',secondLine)
else:
    print(' missing file SearchDirect')
###################### 
my_file = Path("c:/Python34/SystemTCPmod.py")
if my_file.is_file():
    infile = open('c:/Python34/SystemTCPmod.py', 'r')
    firstLine = infile.readline()
    secondLine = infile.readline()
    print ('    SystemTCPmod',secondLine)
else:
    print(' missing file SystemTCPmod')
######################
my_file = Path("c:/Python34/ServerProcess.py")
if my_file.is_file():
    infile = open('c:/Python34/ServerProcess.py', 'r')
    firstLine = infile.readline()
    secondLine = infile.readline()
    print ('    ServerProcess',secondLine)
else:
    print(' missing file ServerProcess')
######################
my_file = Path("c:/Python34/LookupServiceList.py")
if my_file.is_file():
    infile = open('c:/Python34/LookupServiceList.py', 'r')
    firstLine = infile.readline()
    secondLine = infile.readline()
    print ('    LookupServiceList',secondLine)
else:
    print(' missing file LookupServiceList')
######################
my_file = Path("c:/Python34/DirectoriesList.py")
if my_file.is_file():
    infile = open('c:/Python34/DirectoriesList.py', 'r')
    firstLine = infile.readline()
    secondLine = infile.readline()
    print ('    DirectoriesList',secondLine)
else:
    print(' missing file DirectoriesList')
######################

