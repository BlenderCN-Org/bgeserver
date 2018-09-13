# !/usr/bin/env python .
# Created Monday, August 27, 2018 .
# Blender 2.79 clientutils.py
# 
# Last update : 
import base64#######

def stringToBase64(stb64):#
    return base64.b64encode(stb64.encode('utf-8'))#
#
def base64ToString(b64ts):#
    return base64.b64decode(b64ts).decode('utf-8')#
#
def DecodeServer(de):#__________________
    code = de.encode('ascii', 'ignore')#
    de = base64.b64decode(code)#
    return de#
#
def EncodeServer(en):#__________________
    code = en.encode('ascii', 'ignore')#
    en = base64.b64encode(code)#
    return en#
#

#
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
		
		
def reQuotes(data):#________________________________:(
    return str(data).replace('"', ' ').replace('"', ' ')
def setPipes(data):#____________________________________:(
    return str(data).replace('[', '| ').replace(']', ' |')
def cleanlist2(list2):#_____________________________:(
    return str(list2).replace('[', '').replace(']', '')
def remcomma(comma):#_________________:(
    return str(comma).replace(',', ' ')
def addcomma(comma):#_________________:(
    return str(comma).replace('[]', ',')
def whitespace(wspace):#________________
    return str(wspace).replace('[]', ',')
def emptyslot(empty):#_______________:(
    return str(empty).replace('[]', ',')
def bracket(list1):#_____________________________:(
    return str(list1).replace('', '(').replace('', ')')
def rebracket(list1):#_____________________________:(
    return str(list1).replace('(', '').replace(')', '')		
