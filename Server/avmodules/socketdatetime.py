#!/usr/bin/env python
#/ Last Backup / 2017 / Feb / 26 / Current Projects / socketdatetime.py 
#/ Module Breakdown Process Clock Date mods .
import datetime##
import time###### 
class SysDateTime(object):#
    def __init__(self):#_____________________
        self.date = time.strftime("%Y-%m-%d")#
        self.clock = time.strftime("%H:%M:%S")#
        self.second = time.strftime("%S")#
        self.minut = time.strftime("%M")#
        self.hour = time.strftime("%H")#
    def currentdate(self):#
        return self.date#
    def clocktime(self):#
        return self.clock# 
    def currentsec(self):#
        return self.second#
    def currentminut(self):#
        return self.minut#
    def currenthour(self):#
        return self.hour# 
sdt = SysDateTime()#
sdt.currentdate()#
sdt.clocktime()#
sdt.currentsec()#
sdt.currentminut()#
sdt.currenthour()#
