#!/usr/bin/env python
#/ Last Backup / 2017 / Feb / 27 / Current Projects / ThreadingServer101.py  
#/ Module / Endeserver.py
import base64#### 
def DecodeServer(de):#__________________
    code = de.encode('ascii', 'ignore')#
    de = base64.b64decode(code)#            
    return de#
#
def EncodeServer(en):#__________________
    code = en.encode('ascii', 'ignore')#
    en = base64.b64encode(code)#            
    return en#
