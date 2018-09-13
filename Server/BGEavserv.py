#!/usr/bin/env python
#/ Last Update / Sept ,09 ,2017 / Current Projects / ThreadingServer101.py                 
#/ Module SearchDirect.DirectoryFinder for : show_dl = ModuleDirectory(dir_list)/ Update / Mar / 01 / 2017 .
#########################################################################################################################
import ModuleFinder###### Check for Files .
import socket####                                                                                                       #
ipser = ''
#(socket.gethostbyname(socket.gethostname()))
# print (ipser)
import threading#                                                                                                       #
import time######                                                                                                       #
import pyaudio###
import wave######
import datetime##                                                                                                       # 
#import struct####                                                                                                       #
import base64####                                                                                                       #
#import binascii##                                                                                                       #
import os########                                                                                                       #
import sys#######
#_____________________________________________# * * * * * * * * * * * * * #______________________________________________#                                                                                                    #
#_____________________________________________#       Base Modules        # _____________________________________________#
#________________________________________________________________________________________________________________________#
#_____________________________________________# * * * * * * * * * * * * * #______________________________________________#
import mymodule########### for : Setup Module for Testing .                                                                    #
import MainReplies########
import MainRequest########
import ServiceDirectory### for :
import Identifiers########                                         
import SearchDirect####### for : show_dl = ModuleDirectory(dir_list)/ Update / Mar / 01 / 2017 .
import SystemTCPmod#######
import ServerProcess###### for :
import LookupServiceList##
import DirectoriesList#### for :                            -#-
#import ServerSound##############
import socketdatetime##############
#_______________________________________________________________________________________________________________________#
#########################################################################################################################
#________________________                                   -#-
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
#_______________________
class WriteServiceFile:#_____________________________________________________________________________________________________
    def __init__(self, depack):#
        self.items_list = []#
        self.__update(depack)#
        self.file()#_______
    def update(self, depack):#
        self.items_list = depack#
    def file(self):#____
        def conBin(s1):#_______
            return "b'%s'" % s1#______________________
        with open('C:/Projects/Serverlist', 'a') as f:# 
            f.write('\n' + self.items_list)#
    def show(self):#___________
        print(self.items_list)#
    __update = update# 
#__________________________
def WriteServiceList(dirslt, user1):#_____________________________________________________________________________________________________
    with open(dirslt, 'a') as f:# 
        f.write('\n' + user1)#
#__________________________
def WriteSoundInfo(dirslt, user1, file_time):#_____________________________________________________________________________________________________
    file = ('C:/Projects/Soundlist')#   
    info = (' time/sec ')
    with open(file, 'a') as f:# 
        f.write('\n' + user1 + info + str(file_time))#
#_________________________
class DownloadRecordsList:#
    def __init__(self):#
        self.value3 = ()#________________________________________________________
        self.file2 = set(line.strip() for line in open('C:/Projects/Serverlist'))#      
        self.newlist = ("[%s]" % (','.join(self.file2)))#
        self.totalfiles = len(self.file2)#
        value2 = str(' Files/Listed/from://Gstar.Net*')#
        value = str(self.totalfiles)#
        self.value3 = value + value2#
        self.totalrec()#
    def totalrec(self):#
        return self.value3# 
#
class DownloadRecordsFiles:#
    def __init__(self):#
        self.listbuild = []#
        self.server = []#
        self.totalrecords = []#__________________________________________________
        self.file2 = set(line.strip() for line in open('C:/Projects/Serverlist'))#      
        self.serverfiles = []#
        for x in self.file2:#________
            self.listbuild.append(x)#_______________
        self.server = (('\n').join(self.listbuild))#
        en = self.server#__________________
        self.serverfiles = EncodeServer(en)#
    def currentshowSingleRecord(self):#
        return self.serverfiles#
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
def DownLoader(file1):#_______________________________________________________DownLoader
    OBfile = open(file1, 'rb')#
    listfile = OBfile.read()#
    OBfile.close()#
    return listfile#
#
def DownLoader2(file1):#_______________________________________________________DownLoader
    OBfile = open(file1, 'rb')#
    listfile = OBfile.read()#
    OBfile.close()#
    return listfile#
#
def Codec(packet):#___________
    image = open(file1, 'rb')#
    image_read = image.read()#
    image.close()#___________________________________
    image_64_encode = base64.encodestring(image_read)#
    return image_64_encode#
#
def CodecRaw(packet):#_______
    image = open(packet, 'r')#
    image_read = image.read()#
    image.close()#______________________________
    code = image_read.encode('ascii', 'ignore')#
    packet = base64.b64encode(code)#  
    return packet#
#
def Codec_Live(packet):#_______
    image = open(packet, 'rb')#
    image_read = image.read()#
    image.close()#________________________
    packet = base64.b64encode(image_read)#  
    return packet#
#
def DirectoryLoader(file1):#
    Objects = open(file1, 'rb')#
    file1 = Objects.read()#
    Objects.close()#
    return file1#
#
def DirectoryLoader2(file1):#
    Objects = open(file1, 'r')#
    file1 = Objects.read()#
    Objects.close()#
    return file1#
#
def Soundlist(file1):#
    file = ('C:/Projects/Soundlist')# 
    Objects = open(file, 'rb')#
    file1 = Objects.read()#
    Objects.close()#
    return file1#
# . . . . . . . . . . . . . . . . . . . . . . . .
def Requestkey(data):#______________________________Don't Forget to update key count......................
    key = 28# . . . . . . . . . . . . . . . . . . . . . . . .
    for k in range(key):#__________________________
        if data == MainRequest.ServerRequest(k):#___Don't Forget to update key count....
            print('>',ServerProcess.ServerFunc(k))#        
            break
        else:#___Don't Forget to update key count....
            k = 27# Pound Key RETURN. . . . . . . . . . .
    return k#___Don't Forget to update key count....
# . . . . . . . . . . . . . . . . . . . . . . . .
def RequestkeyMenu(data):#____________________
    name = MainRequest.ServerRequest(data)#
    return name#
#
def RequestName(dic):#___________________
    name = ServerProcess.ServerFunc(dic)#
    return name#
#
def DireectoryList():#
    n = 0#
    def func():#
        print('> Directory List :', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#dylls= DireectoryList()#
#dylls.set_n(1)#
#dylls()#
#
def StoreRequestkey():#
    n = 0#_____
    def func():#__________________
        print('> Request key', n)# 
    def get_n():#
        return n#____
    def set_n(value):#
        nonlocal n#
        n = value#_____
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
##dic = Requestkey(key, data)
##dk = StoreRequestkey()
##dk.get_n()
##dk.set_n(dic)
##dk()
#
def FileSizer():#
    n = 0#
    def func():#
        print('> Socket Size >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#fs = FileSizer()#
#fs.set_n(1)#
#fs()#
def NewKey():#
    n = 0#
    def func():#
        print('> Directory Service ', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#nk = NewKey()#
#nk.set_n(1)#
#nk()#
def LoadCurrentDirectory():#
    n = 0#
    def func():#
        print('> Load Cur Dir', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#lcd = LoadCurrentDirectory()#
#lcd.set_n(1)#
#lcd()#
def ServiceDirectories():#
    n = 0#
    def func():#
        print('> Current path > ', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#sdy = ServiceDirectories()#
#sdyset_n(1)#
#sdy()#
#
def DickeyStore():#
    n = 0#
    def func():#
        print('> Dic_Key_ > ', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#dkys = DickeyStore()#
#dkys.set_n(1)#
#dkys()#
#
def DuplicatedFile():#
    n = 0#
    def func():#
        print('> Duplicated File >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#dup = DuplicatedFile()#
#dup.set_n(1)#
#dup()#
#
def pound(data2):#_________
    file = (data2.decode())#. . . . . . . .  .
    de = file#_______________. . . . . . . . . . .
    packet = DecodeServer(de)#. . . . . .. . .. . . . 
    func_out = (packet.decode())#.
    if func_out == '#':#
        print('> func exit')#
        return 1#
    else:#
        return 0#
#
def Open_Mic(root_dir, file_name, file_time, recorder_lock):#
    file_label = (root_dir + file_name)#
    print('> Recording time',file_time)#
    CHUNK = 1024#
    FORMAT = pyaudio.paInt16#. . . . Live Mic. . .
    CHANNELS = 1#
    RATE = 44100#
    WAVE_OUTPUT_FILENAME = file_label#. . . . Live Mic. . .
    WIDTH = 2#. . . . Live Mic. . .
    frames = []#. . . . Live Mic. . .
    p = pyaudio.PyAudio()#
    stream = p.open(format = p.get_format_from_width(WIDTH),
                    channels = CHANNELS,
                    rate = RATE,
                    output = True,
                    frames_per_buffer = CHUNK)#. . . . Live Mic. . .
    HOST = ipser#_____________________________Symbolic name meaning all available interfaces
    PORT = 1236#_________________________________________Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#
    s.bind((HOST, PORT))#
    s.listen(1)#
    conn, addr = s.accept()#
    print ('> Mic ON *', addr)#. . . . Live Mic. . .
    data = conn.recv(1024)#
    print('> set rec time')#
    sdt = SysDateTime()#
    a = datetime.datetime(100,1,1,int(sdt.currenthour()),int(sdt.currentminut()),int(sdt.currentsec()))#
    b = a + datetime.timedelta(0,int(file_time))# days, seconds, then other fields.
    sdt = SysDateTime()#
    print('> Start time ', sdt.clocktime())#
    while True:#
        stream.write(data)#
        data = conn.recv(1024)#. . . . Live Mic. . .
        frames.append(data)#
        sdt = SysDateTime()#
        time_string = (sdt.clocktime())#
        if str(time_string) == str(b.time()):#
            print('> Finish time ', sdt.clocktime())# . . . Live Mic. . .
            stream.stop_stream()#
            stream.close()#
            p.terminate()#
            conn.close()#
            break#
    if recorder_lock == 1:#______________________
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')#. . . . Live Mic. . .
        wf.setnchannels(CHANNELS)#
        wf.setsampwidth(p.get_sample_size(FORMAT))#
        wf.setframerate(RATE)#
        wf.writeframes(b''.join(frames))#
        wf.close()#    
    print('> Mic OFF *', addr)#. . . . Live Mic. .
    print('>',file_label)#
    print('> Recorded time',file_time,'sec.')#
#
def File_Label():######_____________________________________________________
    print('test')#
#
def Upload_keys(codec_buffer):#________________________loop_keys
    if codec_buffer in loop_keys:#
        print('loop_keys')#
        return codec_buffer#
#
def Auto_Codec(depack):####### # # # # # # # # # # # # # # # # #____________________________________
    if '.png' in depack:#
        print('> Download .png')#
        return 1# . . . . . . . . . . . . . . . . . . . . . . . .
    elif '.txt' in depack:#
        print('> Download .txt')# 
        return 0#  . . . . . . . . . . . . . . . . . . . . . . . .      
    elif '.wav' in depack:#
        print('> Live mic')#
        return 2#  . . . . . . . . . . . . . . . . . . . . . . . .
    elif '.py' in depack:#
        print('> Download .py')#
        return 0#  .
    else:# . . . . . . . . . . . . . . . . . . . . . . . .
        print('> Download .txt')#        
        return 0# . . . . . . . . . . . . . . . . . . . . . . . .
#
def Menu(name, key):#___________________________________________________________________________________________________
    def func0(key):#_________________
        print ('> No func0 >')#
        key = 0 #
        return key#
    def func1(key):#_________________
        print ('> Go ahead func1 >')#
        key = 7# 
        return key#___________________
    def func2(key):#_________________
        print ('> Go ahead func2 >')#
        key = 8# 
        return key#___________________
    def func3(key):#_________________
        print ('> Go ahead func3 >')#
        key = 9# 
        return key#________________
    menu = {            '#' : func0,
            'get file size' : func1,
            'set codec'     : func2,
            'server name'   : func3,
            }#______
    functocall = menu[name]#
    key = functocall(key)#
    return key#
#
def List_Func(key):#________________________________________________________________________________________________________
    print('> List_Func .')#
    tester = DirectoriesList.Listings(key)#.
    return tester#
#
def Downloads_Func(key):#________________________________________________________________________________________________________
    print('> Downloads .')#________________
    tester = DirectoriesList.Listings(key)#
    return tester#
#
def ModuleDirectory(dir_list):#
        dir_list = []#
        for k in range(8):## Don't Forget to Update Directory key Count. . . . . . . . . . . . . . . .
            dir_list.append(SearchDirect.DirectoryFinder(k))#
            ser_dirs = (('\n').join(dir_list))#
        return ser_dirs#   
#
def DirectoryLookup_Func(key):#________________________________________________________________________________________________________
    print('> Search Direct .')#________________
    tester = SearchDirect.DirectoryFinder(key)#
    return tester#
#
def ServiceDirectory_Func(key):#________________________________________________________________________________________________________
    print('> Service Directory .')#__________________
    tester = ServiceDirectory.DirectoryListings(key)#
    return tester#
#
class ChangeDirectory:#_________
    def __init__(self, packet):#
        self.packet = []#____
        self.__update(packet)#
    def update(self, packet):#
       self.packet = packet
    def show(self):#________
        return(self.packet)#____
    def currentdirectory(self):#
        return(self.packet)#        
    __update = update#
#
class ServerDefaultDirect:#_____
    def __init__(self, packet):#
        self.defaultpath  = []#
        self.__update(packet)#
    def update(self, packet):#___
       self.defaultpath = packet#
    def showserverpath(self):#_______
        print ('>',self.defaultpath)#
    def serverpath(self):#_____
        return self.defaultpath#
    __update = update#
#
class StreamLock:#____________
    def __init__(self, lock):#
        self.lock = lock#___
        self.__update(lock)#
    def update(self, lock):#
        self.lock = lock#
    def showlock(self):#
        return self.lock#
    __update = update#
#
def Addmin():
    n = 0#
    def func():#
        print('> Addmin_key >', n)# 
    def get_n():#
        return n#
    def set_n(value):#
        nonlocal n#
        n = value#
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#
class ThreadedServer(object):#_____
    def __init__(self, host, port):#
        self.host = host#
        self.port = port#____________________________________________
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#
        self.sock.bind((self.host, self.port))#
        print(self.host, self.port)# 
    def listen(self):#______
        self.sock.listen(5)#
        while True:#___________________________
            client, address = self.sock.accept()#
            client.settimeout(None)#_______________________________________________________
            threading.Thread(target = self.listenToClient,args = (client,address)).start()#
    def listenToClient(self, client, address):#
        socket_size = 4096#
        self.client = client#
        self.address = address#
        socket_default_size = 4096#
        fs = FileSizer()#. . . . . . .
        fs.set_n(socket_default_size)#. . .
        fs()#. . . . . . . . . . . . . . . . . . 
        file_size = fs.get_n()#. . . . . . . . .
        sysCycle = (0)#
        picsCycle = (0)#
        sysAddminREC = (0)#C:/Projects/Projects/
        packet = ('C:/Projects/Projects/')#_ _ _ _ _Initialize. default.       C:/Projects/ServerAddmin/
        cdl = ChangeDirectory(packet)#
        cdl.update(packet)#
#       __________________________
        sdy = ServiceDirectories()#
        sdy.set_n(cdl.currentdirectory())#
#       ______________________________
        pcd = Identifiers.Pics_Codec()#. . . . . . . . . . 
        pcd.set_n(0)#. . . . . . . . . . 
        pcd()#. . . . . . . . . . . . . . . . 
#       __________________________
        codec_buffer = pcd.get_n()#.. . . . . . . . . .
#       _________________________________
        sdd = ServerDefaultDirect(packet)#
#       ____________________
        dkys = DickeyStore()#
        dkys.set_n(1)#
        dkys()#
        syslk = Identifiers.SystemLocks()#. .
        syslk.set_n(0)#.
        sdt = SysDateTime()#
        recorder_lock = 0
        while True:#____________________________________________
            def Duplicated_File():#
                print(' Duplicated File')#
            try:#_______________________________________________
                socket_size = int(fs.get_n())#
                data = client.recv(socket_size)#________
                if data:#_______________________________________
                    dic = Requestkey(data)#_____________________
                    dk = StoreRequestkey()#_____________________
                    dk.set_n(dic)#______________________________
                    dk()#_______________________________________
                    if dic == 21:#_______________________________________________________________________________________
                        dk.set_n(0)#___________________________________
                        client.send(MainReplies.ServerReplies(dic))# . . . . . . . . get file size. . . . . . . . . . 
                        while True:#_________________. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                            data = client.recv(socket_size)# . . . . . . . . get file size. . . . . . . . . . . . . . . . . . .  
                            if data:#___________________. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                name = RequestName(dic)# . . . . . . . . get file size. . . . . . . . . . . . . . . . .
                                key = 0#______________. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 
                                des = Menu(name, key)# . . . . . . . . get file size. . . . . . . . . . . . . . . . . .
                                nk = NewKey()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                nk.set_n(des)# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                nk()#__________________. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                                file = (data.decode())#. . . . . . .  . . . . . . . . get file size. . . . . . . . . . .
                                de = file#_______________. . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                packet = DecodeServer(de)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                depack = (packet.decode())#. . . . . . . . . get file size. . . . . . . . . . . . . . . .
                                user1 = depack#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                                name = cdl.show()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                                key = LookupServiceList.ServiceList(name)# . . . . . . . . . . . . . . . . . . . . . . .
                                tester = List_Func(key)# . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . .
                                file1 = tester#_______________ . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                dtyldr = DirectoryLoader(file1)#. . . .  . . . . . . . get file size. . . . . . . . . . .
                                unpack = (dtyldr.decode())# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                if user1 in unpack:#_____ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    user2 = (name + user1)#_______. . . . get file size. . . . . . . . . . . . . . . . .
                                    size = os.path.getsize(user2)#. . . . . . . . . . . . . . . .  . . . . . . . . . . .  
                                    filesize = str(size)#____________ . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    quote = (' bytes for download .')# . . . . . . . get file size. . . . . . . . . . . .
                                    reply = (' Request file size ')#... . . . . . . . . . . . . . . . . . . . . . . . .  .
                                    en = (reply + filesize + quote)#. . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    packet = EncodeServer(en)# . . . . . . . get file size. . . . . . . . . . . .. . .  .
                                    client.send(packet)#. .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    break# . . . . . . . get file size. . . . . . . . . . . . get file size. . . . . . 
                                else:#___________________________________________. . . . . . . . . . . . . . . . . . . .
                                    client.send(MainReplies.ServerReplies(10))# . . . get file size. . . . . . . . . .
                                    inv = Invalid()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    inv.set_n(1)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    inv()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    break# . . . . . . . get file size. . . . . . . . . . . . get file size. . . . . . . . .
                    elif dic == 22:#____________________________________________________________________________________
                        dk.set_n(0)#___________________________________
                        client.send(MainReplies.ServerReplies(dic))#
                        pcd = Identifiers.Pics_Codec()#. . . . . . . . . . 
                        pcd.set_n(1)#. . . . . . . . . . 
                        pcd()#.  . . . . . . . . . . . .
                    elif dic == 1:#______________________________________________________________________________________
                        dk.set_n(0)#___________________
                        MainRequest.ServerRequest(1)#____
                        client.send(MainReplies.ServerReplies(1))#
                        syslk = Identifiers.SystemLocks()#. . . . 
                        syslk.set_n(1)#. . . . . .
                        syslk()#. . . . . . . . .
                        sysCycle = syslk.get_n()#________________________________________________________________________
                        addmin = Addmin()#
                        addmin.set_n(1)#
                        addmin()#
                    elif dic == 9:#______________________________________________________________________________________
                        dk.set_n(0)#___________________
                        MainRequest.ServerRequest(9)#
                        enter = Identifiers.EnterRec()#. . . . .Menu
                        enter.set_n(1)#. . . . . . .
                        enter()#. . . . . . . . . . . .
                        client.send(MainReplies.ServerReplies(2))#____________________________________________________
                    elif dic == 2:#______________________________________________________________________________________
                        dk.set_n(0)#____________________
                        MainRequest.ServerRequest(2)#______________________________________________________
                        td = Identifiers.TimeDate()# . . . . Time Date.
                        td.set_n(1)#. . . . . Time Date.
                        td()#. . . . . . . . 
#                        sdt = SysDateTime()#. . . . . . . . . . . . . . . . . . . ..
                        en = socketdatetime.sdt.clocktime()#
                        packet = EncodeServer(en)# .. . . . . . . . . . . . . . . . . .Time Date.
                        client.send(packet)#______________________________________________________________________________
                    elif dic == 3:#______________________________________________________________________________________
                        client.send(MainReplies.ServerReplies(10))#. . . . . . . . . . . . . . . . . . . . . . . . . .
                        inv = Identifiers.Invalid()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        inv.set_n(1)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        inv()#.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  
                    elif dic == 4:#______________________________________________________________________________________
                        dk.set_n(0)#___________________
                        MainRequest.ServerRequest(4)#.. . . . . .Lookup Rec . . . . . Lookup Rec  . . . . . 
                        lur = Identifiers.LookupRec()#. . . . . . .  . . . .Lookup Rec . . . . . . Lookup Rec  . . . . .
                        lur.set_n(1)#. . . . . . . . . . .  . . . .Lookup Rec . . . .. . . . . . . . Lookup Rec  . . . . 
                        lur()#. . . . . . . . . . . . . .  . . . .Lookup Rec . . . . . . . . . .. . Lookup Rec  . . . .  
                        en = cdl.currentdirectory()#. .  . . . .Lookup Rec . . . . . . . . . . . . . Lookup Rec  . . .   
                        codec = EncodeServer(en)#. .  . . . .Lookup Rec . . . . . . . . . . . . . . . Lookup Rec  .  . . 
                        client.send(codec)#______________________________________________________________________________
                    elif dic == 5:#______________________________________________________________________________________    
                        dk.set_n(0)#____________________
                        MainRequest.ServerRequest(5)#. . . . . . . . . . . . . .. . . . . . . .Upload Records.
                        while True:#_____________________. . . . . . . . . . . . . . . . . . . .   . .Upload Records.
                            ulr = Identifiers.UploadRec()#. . . . .. . . . .. . . . . . . . . . . . . .Upload Records.
                            ulr.set_n(1)#. . . . . . . . . . . . .Upload Records.. . . .. . . . .  . . .Upload Records.
                            ulr()#. . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .. . . .Upload Records.
                            client.send(MainReplies.ServerReplies(5))#. . . . . .. . . . . . . . ..  .Upload Records.
                            data = client.recv(socket_size)#. . . . . . .Upload Records.. . .  .Upload Records.
                            if data:#__________________. . . . . . .Upload Records.. . .. . . . . . . .Upload Records.
                                file = (data.decode())#. . . . . . .Upload Records.. . . . . .  . . .. .Upload Records.
                                de = file#_______________. . . . . . .Upload Records.. . . . . . .. .  . .Upload Records.
                                packet = DecodeServer(de)#. . . . . . .Upload Records.. . .. . . . . . .Upload Records.
                                depack = (packet.decode())#. . . . . . .Upload Records.. . . . . . . .. .Upload Records.
                                user1 = depack#______________________________. . . . .. . . . . . . . . .Upload Records.
                                dylls = DireectoryList()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                                dylls.set_n(1)# . . . . . . . . . . . . . . > list . . . > list . . . > list.  . . > list . . . 
                                dylls()# . . . . . . . . . . . . . . . > list . . . > list . . . > list.  . . > list . . . . . .
                                name = cdl.show()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                key = LookupServiceList.ServiceList(name)#. . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                tester = List_Func(key)# . . . . . . . . . . . . . . . . . > list . . . > list . . . > list.  . . > list . . 
                                doubles_check = set(line.strip() for line in open(tester))# . . . . doubles. . . . . . . .
                                if user1 in doubles_check:#. . . . . . . Duplicate File Checher . . . . . . . . . . . . .
                                    dup = DuplicatedFile()# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    dup.set_n(0)#. . . . . . Duplicate File Checher . . . . . . . . . . . . . . . . . . .
                                    dup()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                  
                                    client.send(MainReplies.ServerReplies(24))#. . . . . . . . . . . . . . . . . . . .
                                    break#. . . . . . Duplicate File Checher . . Duplicate File Checher . . . . . . . . .
                                else:#. . . . . . . . Process Upload . . . . . . . .Process Upload . . . . . . . . . . . .
                                    client.send(MainReplies.ServerReplies(6))#. . . . . . .Upload Records.
                                    self = cdl.show()#_________________. . . . . . . . . . . . ... .Upload Records.
                                    fileobj = open(self + depack, 'w+')# . . . . . . . . . . . . . .. .Upload Records.
                                    fileobj.write('setup')#. . . . . .. . . . . . . . . . . . . . . . .Upload Records.
                                    fileobj.close()#. . . . . . .Upload Records.. . . . . .. . . . .Upload Records.
                                    fs()#. . . . . . . . . . . . . .. . . . . . . . . . . . . . . .Upload Records.
                                    ans = Auto_Codec(depack)#.... . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    codec_buffer = (ans)#....... .. . . . . . . . . . . . . . . .Upload Records.
                                    data3 = client.recv(socket_size)#. . . . . . .Upload Records.. . . . .. . . . .Upload Records.
                                    if codec_buffer == (0):#. . . . . . .Upload Records.. . . . . . .Upload Records.
                                        if data3:# Standard Uploads . Text files .
                                            client.send(MainReplies.ServerReplies(7))#. . .. . .Upload Records.
                                            wsf = WriteServiceFile(self + depack)#. . . . . . . . . . . .Upload Records.
                                            key = LookupServiceList.ServiceList(self)#. . . . . . . . . . . .Upload Records.
                                            dirlk = DirectoryLookup_Func(key)#. . . . . . . . . . . .Upload Records.
                                            de = (data3.decode())#. . . . . . . . . .. . . . . . . . . . . . .Upload Records.
                                            codec = DecodeServer(de)#. . . . . . . . .. . . . . . . . . . . . .Upload Records.
                                            dirslt = ServiceDirectory_Func(key)#. . .. . . . . . . . . . . . . .Upload Records.
                                            wsl = WriteServiceList(dirslt, depack)#. . . . . . . . . . . . . . .Upload Records.
                                            with open(self + depack, 'w') as f:#. . . . .. . . . . . . . . . . .Upload Records.
                                                f.write(codec.decode())#. . . . .. . . . . . . . . . . . . . . .Upload Records.
                                                break##. . . ..Upload Records  .  . . .Upload Records... . . ..Upload Records.
                                    elif codec_buffer == (1):#. png / jpg
                                        if data3:# Standard Uploads . Text files .
                                            pcd.set_n(0)#. . . . . . . . . .. . . . . .. . . . . . . . . . . . .Upload Records.
                                            image_64_decode = base64.decodestring(data3)# . . . . . . .Upload Records.
                                            client.send(MainReplies.ServerReplies(7))#. . . . . . .Upload Records.
                                            wsf = WriteServiceFile(self + depack)#. . . . . . .Upload Records.
                                            svl = LookupServiceList.ServiceList(self)#_______________. . .. .Upload Records.
                                            dirslt = ServiceDirectory_Func(svl)#(svl)#. . . . .Upload Records.
                                            wsl = WriteServiceList(dirslt, user1)#. . . . . . .Upload Records.
                                            image_result = open(self + depack, 'wb')# . . . . . . . . . . . .Upload Records.
                                            image_result.write(image_64_decode)#. . . . . . .Upload Records.
                                            image_result.close()#   . . . . . . . . . . . . . . . . . . . . . . . .                                               refresh_keys()
                                            break#____________.Upload Records.. . . . . . .Upload Records.
                                    elif codec_buffer == (2):#. tester . . . . . . . . . . . . . . . . . . . . . . . .
                                        if data3:#  . . . . . . . . . . . . . . . . . . . . . . . .
                                            client.send(MainReplies.ServerReplies(7))#. . .. . .Upload Records.
                                            wsf = WriteServiceFile(self + depack)#. . . . . . . . . . . .Upload Records.
                                            key = LookupServiceList.ServiceList(self)#. . . . . . . . . . . .Upload Records.
                                            dirlk = DirectoryLookup_Func(key)#. . . . . . . . . . . .Upload Records.
                                            de = (data3.decode())#. . . . . . . . . .. . .  . . . . .Upload Records.
                                            codec = DecodeServer(de)#. . . . . . . . .. . . . . . . . . . . . .Upload Records.
                                            dirslt = ServiceDirectory_Func(key)#. . .. .. . . . . . . .Upload Records.
                                            wsl = WriteServiceList(dirslt, depack)#. . . . . . . . . . . . . . .Upload Records.
                                            with open(self + depack, 'wb') as f:#. . . . .. . . . . . . . . . . .Upload Records.
                                                f.write(data3.decode())#. . . . .. . . . . . . . . . . . . . . .Upload Records.
                                                break#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    else:#____________________________________________. . . . . . .Upload Records.
                                        client.send(MainReplies.ServerReplies(10))#. . . . . . .Upload Records.
                                        break#___________________________________________________________________________
                    elif dic == 6:#______________________________________________________________________________________
                        dk.set_n(0)#___________________ . . . . . . . . . . . . . . . . . . . . . . . .
                        MainRequest.ServerRequest(6)#. . . . . . . . . > Downloads.. . . . . > Downloads. . .
                        dlr = Identifiers.DownloadRec()#. . . . . > Downloads.. . . . . > Downloads. . . . . . . . . . .   
                        dlr.set_n(1)#. . . . . . . .  . . . . > Downloads.. . . . . > Downloads. . . . . . . . . . . . .
                        dlr()#. . . . . . . . . . . .  . . . . > Downloads.. . . . . > Downloads. . . . . . . . . . . . .
                        name = cdl.show()# . . . > Downloads.. . . . . > Downloads. . .  . . . . . . . . . . . . .. . . .
                        key = LookupServiceList.ServiceList(name)# . . . > Downloads.. . . . . > Downloads. . . . . . .
                        servicelist = Downloads_Func(key)# .  . . . > Downloads.. . . . . > Downloads. . . . . . . . . .
                        client.send(MainReplies.ServerReplies(8))# . . . . > Downloads.. . . . . > Downloads. . . . . 
                        data = client.recv(socket_size)# . . . . > Downloads.. . . . . > Downloads.  . > Downloads. . . . . . .
                        if data:#_______________________ . . . . > Downloads.. . . . . > Downloads. . . . . . . . . . . .
                            clientfile = (data.decode())# . . . . > Downloads.. . . . . > Downloads.  . > Downloads.
                            de = clientfile#_________ . . . . . . . . . . . . . > Downloads.. . . . . >
                            packet = DecodeServer(de)# . . . . . . . . . . . . . > Downloads.. . . . . > . > Downloads.
                            file4 = (packet.decode())#  . . . . . . . . . . . . . > Downloads.. . . . . > . > Downloads.
                            file1 = servicelist# . . . . . . . . . . . . . > Downloads.. . . . . >
                            dtyldr = DownLoader2(file1)#. . . . > Downloads.. . . . . > Downloads.  . > Downloads.
                            file3 = dtyldr.decode()#### . . . . . . . . . . . . . > Downloads.. . . . .. . . . . .. . >
                            depack = file4#__________  . . . . . . . . . . . . . . . . . . . . . . . .
                            ans = Auto_Codec(depack)#... . . . . . . . . . . . . . . . . . . . . . . . .
                            codec_buffer = (ans)#....... . . . . . . . . . . . . . . . . . . . . . . . .
                            if file4 in file3:#________ . . . . . . . . . . . . . > Downloads.. . . . . . . . . . .. . >
                                if codec_buffer == (0):# . . . . . . . . . . . . . > Downloads.. . . . . . . . . . .. . >
                                    name = (name + file4)# . . . . > Downloads.. . . . . >. . . > Downloads.. . . . . >
                                    packet = str(name)# . . . . . . . . . . . . . > Downloads.. . . . . >
                                    codec = CodecRaw(packet)# . . . . . . .  . . . . .. . . . . . > Downloads.. . . . . >
                                    client.send(codec)# . . . . . . . . . . . . . > Downloads.. . . . . . . . . . . . . >
                                if codec_buffer == (1):# . . . . . . . . . . . . . > Downloads.. . . . . >
                                    pcd.set_n(0)#. . . . . . . . . . > Downloads.. . . . . > Downloads.  . > Downloads.
                                    name = (name + file4)# . . . . > Downloads.. . . . . >. . . > Downloads.. . . . . >
                                    packet = str(name)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    dl = Codec_Live(packet)# . . . . > Downloads.. . . .  . . . . . . . . . . . . . . . . .. >
                                    client.send(dl)# .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                                if codec_buffer == (2):# . . . . . . . . . . . . . > Downloads.. . . . . >
                                    pcd.set_n(0)#. . . . . . . . . . > Downloads.. . . . . > Downloads.  . > Downloads.
                                    name = (name + file4)# . . . . > Downloads.. . . . . >. . . > Downloads.. . . . . >
                                    packet = str(name)
                                    dl = Codec_Live(packet)# . . . . > Downloads.. . . .  . . . . . . . . . . . . . . . . .. >
                                    client.send(dl)#. . . . > Downloads.. .. . . . . . . . . . . . . . .. . . >                                    client.send(dl)#. . . . > Downloads.. .. . . . . . . . . . . . . . .. . . >
                                if codec_buffer == (3):# . . . . . . . . . . . . . > Downloads.. . . . . . . . . . .. . >
                                    name = (name + file4)# . . . . > Downloads.. . . . . >. . . > Downloads.. . . . . >
                                    packet = str(name)# . . . . . . . . . . . . . > Downloads.. . . . . >
                                    codec = CodecRaw(packet)# . . . . . . .  . . . . .. . . . . . > Downloads.. . . . . >
                                    client.send(codec)# . . . . . . . . . . . . . > Downloads.. . . . . . . . . . . . . >
                            else:#___________________________________________ . > Downloads.. .. . . . . . . . . . . .
                                client.send(MainReplies.ServerReplies(10))# . . . . . . .. . > Downloads.. . . . . >
                                inv = Identifiers.Invalid()#. . . . . . . . . . . . . . > Downloads.. . . . . . . . . . >
                                inv.set_n(1)#. . . . . . . . . . . . . . . . . . . . . > Downloads.. . . . . . . . .  . >
                                inv()#___________________________________________________________________________________
                    elif dic == 7:#_______________________________________________________________________________________
                        dk.set_n(0)#____________________. .. . . . . . . . . . . . . . . . .. . . .
                        MainRequest.ServerRequest(7)#. .. . . . . . . . . . . . . . . . .. . . .
                        ltr = Identifiers.ListRec()#. . . .. . . . . . . . . . . . . . . . .. . . . . . . . show list
                        ltr.set_n(1)#. . . . . . . . . . . . . . . . . . show list . . . . . . . . . . . . . .
                        ltr()#_____________________ . . . . . . . . . . . .  . . . . . . .. . . . show list . . . . . ..
                        dlr = DownloadRecordsList()#. . . . . . . . . . . . . . . . . . . show list . . . . . . . . ..         
                        en = dlr.totalrec()#____.. show list. . . . . show list . . . . . show list  . . . . . show list 
                        codec = EncodeServer(en)#. . . . . . . . . . . . . . . . . . . show list . . . . . . . . . . . . .
                        client.send(codec)#______________________________________________________________________________
                    elif dic == 11:#_____________________________________________________________________________________
                        dk.set_n(0)#_____________________ . . . . . . . . . . . . . . . . . . . . . . . .
                        MainRequest.ServerRequest(11)#... show dir . . . . . show dir . . . . . show dir . . .
                        md = Identifiers.DirList()#. . . . . .. show dir . . . . . show dir . . . . . show dir . . .
                        md.set_n(1)#. . . . . . . .. show dir . . . . . show dir . . . . . show dir . . . <<<<<<<<<<
                        md()#_______________________________ . . . . show dir . . . . . show dir . . . <<<<<<<<<<
                        dir_list = cdl.currentdirectory#show dir . . . <<<<<<<<<<
                        show_dl = ModuleDirectory(dir_list)# . show dir . . . . . show dir . . . <<<<<<<<<<
                        en = show_dl#____________
                        codec = EncodeServer(en)#. show dir . . . . . show dir . . . . . show dir . . . <<<<<<<<<<
                        client.send(codec)#______________________________________________________________________________
                    elif dic == 8:#______________________________________________________________________________________
                        dk.set_n(0)#____________________ . . . . . . . . . . . . . . . . . . . . . . . .
                        MainRequest.ServerRequest(8)#. . . . . . . . . . . . . . . . .Directory Change!   <<<<<<<<<
                        while True:#____________________#. . . . . . .. . . . . . . . . . . . . . . Directory Change!
                            dc = Identifiers.DirChange()#. . . . . . . . . . .  . . . .. . . . Directory Change!  
                            dc.set_n(1)#. . . . . . . . . . . . . . . . . .  . . . . . .. . .Directory Change!    
                            dc()#. . . . . . . . . . . . . . . . . . . . . . .  . . . . .Directory Change!    
                            client.send(MainReplies.ServerReplies(9))# . . . . . . . . .  . . . . .Directory Change!
                            data = client.recv(socket_size)#. . . . . . . . . . . . . . . . . . . . .
                            if data:#__________________. . . . . . . . . . . . . . . . . . . . .
                                change = (data.decode())#. . . . . . . . . . . . . . . . . . . . .
                                de = change#_______________ . . . .  . . . . .Directory Change!
                                precode = DecodeServer(de)#. . . . . . . . . . . . . . . . . . . . .
                                packet = precode.decode()#. . . . . . . . . . . . . . . . . . . . .
                                dir_list = cdl.currentdirectory()#
                                show_dl = ModuleDirectory(dir_list)# . . . . . . . . . . . . . . . . . . . .
                                lookin = packet[:12]#. . . . . . . . . . . . . . . . . . . . .
                                if lookin == ('C:/Projects/'):#   . . .  . . . . .Directory Change!                             
                                    if packet in show_dl:# . . . . . . . . . . . . . . . . . . . . .
                                        sdd = ServerDefaultDirect(packet)#_____.  . . . . .Directory Change! 
                                        sdd.showserverpath()#. . . . . . . . . . . . . . . . . . . . .
                                        de = change#______________. . . . . . . . . . . . . . . . . . . . .
                                        precode = DecodeServer(de)# . . . .  . . . . .Directory Change!
                                        packet = precode.decode()#. . . . . . . . . . . . . . . . . . . . .       
                                        cdl.update(packet)#________________. . . . . . . . . . . . . . . . . . . . .
                                        client.send(MainReplies.ServerReplies(11))#. . . . . . .  . . . . . . . . . .
                                    else:#___________________________________________
                                        client.send(MainReplies.ServerReplies(10))#.  . . . . .Directory Change! 
                                        inv = Identifiers.Invalid()#. . . . . . . .
                                        inv.set_n(1)#. . . . . .. . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . .
                                        inv()#. . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . .  . . . .
                                else:#___________________________________________
                                    client.send(MainReplies.ServerReplies(10))#.  . . . . .Directory Change! 
                                    inv = Identifiers.Invalid()#. . . . . . . .
                                    inv.set_n(1)#. . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    inv()#. . . . . . . . . . . . . .  . . .Directory Change!   <<<
                                break#___________________________________________________________________________________
                    elif dic == 12:#_____________________________________________________________________________________
                        client.send(MainReplies.ServerReplies(10))#. . . . . . . . . . . . . . . . . . . . . . . . . .
                        inv = Identifiers.Invalid()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        inv.set_n(1)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        inv()#. 
                    elif dic == 15:#_____________________________________________________________________________________
                        dk.set_n(0)#_____________________
                        MainRequest.ServerRequest(15)#. . . . . > list . . . > list . . . > list.#
                        dylls = DireectoryList()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        dylls.set_n(1)# . . . . . . . . . . . . . . > list . . . > list . . . > list.  . . > list . . . 
                        dylls()# . . . . . . . . . . . . . . . > list . . . > list . . . > list.  . . > list . . . . . .
                        name = cdl.currentdirectory()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        key = LookupServiceList.ServiceList(name)#. . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        tester = List_Func(key)# . . . . . . . . . . . . . . . . . > list . . . > list . . . > list.  . . > list . . 
                        file1 = tester#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        dtyldr = DirectoryLoader(file1)#. . . . . . . . > list . . . > list . . . > list. . . . . . .
                        en = (dtyldr.decode())#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        codec = EncodeServer(en)#. . . . . . . . > list . . . > list . . . > list. . . . . . . . . . . 
                        client.send(codec)#_____________________________________________________________________________ 
                    elif dic == 16:#.___________________________servicelist________________________servicelist___________
                        dk.set_n(0)#____________________. . . . . . . . . .. . . . . . .... .. .. ... . . . . . .. . . . 
                        MainRequest.ServerRequest(16)#. .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        dwnldsl = DownloadRecordsFiles()#________. . . > servicelist  . . .  > servicelist . . . . . . . 
                        codec = dwnldsl.currentshowSingleRecord()#. . . > servicelist  . . .  > servicelist . . . . . . .
                        client.send(codec)#__________________________servicelist________________________servicelist . . . 
                    elif dic == 17:#____________________________________________________________________________________
                        dk.set_n(0)#____________________ . . . . . . . . . . . . . . . . . . . . . . . .
                        MainRequest.ServerRequest(17)# . . . . . . . . . . . . . . . . . . . . . . . .
                        mod001 = Identifiers.ModuleLoader()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        mod001.set_n(1)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        mod001()#____________________________________ . . . . . . . . . . . . . . . . . . . . . . . .
                        client.send(MainReplies.ServerReplies(18))# . . . . . . . . . . . . . . . . . . . . . . . .
                        mymodule.sayhi()#________________________________________________________________________________
                    elif dic == 0:#______________________________________________________________________________________
                        dk.set_n(0)#____________________ . . . . . . . . . . . . . . . . . . . . . . . .
                        MainRequest.ServerRequest(0)#. . . . . . . . . . . . . . . . . . . . . . . . .
                        client.send(MainReplies.ServerReplies(0))#____________________________________________________
                    elif dic == 20:#_____________________________________________________________________________________
                        dk.set_n(0)#.___________________. . socket size. . . socket size. . . socket size. 
                        MainRequest.ServerRequest(20)#.___________ . . . . . . . . . . . . . . . . . . . . . . . .
                        client.send(MainReplies.ServerReplies(20))#. . . . .. . socket size. 
                        data2 = client.recv(socket_size)#. . . . . . . . socket size. 
                        if data2:#______________  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                    
                            de = data2.decode()#. . . . . . .. . socket size. . . . . . . . . . . . . . . . . . . . . . .
                            codec = DecodeServer(de)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                            size = (codec.decode())#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                            check_integer = size.isdigit()#. . . . . . . . . . . . . .
                            if check_integer == True:#. . . . . . . . . . . . . . . . . . . . . . . . . .
                                pass#. . . . . . . . . . . . . . . . . . . . . . . . . .
                                limit = int(size)# . . . . . . . . . . . . . . . . . . . . . . . .
                                if limit >= 3 and limit <= 2048:# . . . . . . . . . . . . . . . . . . . . . . . .
                                    print('> socket size pass')# . . . . . . . . . . . . . . . . . . . . . . . .
                                    pass# . . . . . . . . . . . . . . . . . . . . . . . .
                                    fs = FileSizer()#. . . . . . . . . . . . .. . socket size. . . socket size. 
                                    fs.set_n(size)#. . . . . . . . . . . . . .
                                    fs()#. . . . . . . . . . . . . . . . . . . . . socket size. 
                                    socket_size = fs.get_n()#. . . . . . . . . . 
                                    filesize = str(size)#. . . . . . . . . . . . . . . . . . . . . . . . . .. . socket size. 
                                    quote = (' bytes .')# . . . . . . . socket size. . . . . . . . . . .
                                    reply = (' Requested file sizer ')#... . . . . . . . . . . . . . . . . . . . . . . . .  .
                                    en = (reply + filesize + quote)#. . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    packet = EncodeServer(en)# . . . . . . .. . socket size.  . . . . . . . . .. . .  .
                                    client.send(packet)#._______________________________________________________________________ 
                                else:#____________________________________________ . . . . . . . .
                                    client.send(MainReplies.ServerReplies(10))#. . . . . . . . . . . . . . . .
                                    inv = Identifiers.Invalid()#. . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    inv.set_n(1)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . 
                                    inv()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                            else:#____________________________________________ . . . . . . . .
                                client.send(MainReplies.ServerReplies(10))#. . . . . . . . . . . . . . . .
                                inv = Identifiers.Invalid()#. . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                inv.set_n(1)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . 
                                inv()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                    elif dic == 10:#______________________________________________________________________________________
                        dk.set_n(0)#____________________. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        MainRequest.ServerRequest(10)#___________. . . . . . . . . . . . . . . . . . . . . . . . . . .
                        client.send(MainReplies.ServerReplies(23))#. . . . . . . . . . . . . . . . . . . . . . . . . .
                    elif dic == 23:# . . . . . . . . . . . . Live Mic. . . . . .. . . . Live Mic. . ..  . Live Mic. . .
                        dk.set_n(0)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        while True:#_______________. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                            sysCycle = syslk.get_n()#___________________. . . . . . . . . . . . . . . . . . . . . . . . . 
                            client.send(MainReplies.ServerReplies(25))#_. . . . Live Mic. . . . . . . . . . . . . . . .
                            MainRequest.ServerRequest(23)#. . . . . . . . . . . . . Live Mic. . . . . . . . . . . . . . .
                            data = client.recv(socket_size)#. . . . . . . . . . . . . . . . . . . . . . . . . . .
                            if data:#_______________. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                file = (data.decode())#. . . . . ... . . . Live Mic. . . . . . . . . . . . . . . . . . . .
                                de = file#_______________. . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . 
                                packet = DecodeServer(de)#. . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . .
                                file_name = (packet.decode())#. . . . . .. . . . . . . .. . . . . . . . . . . . . . . . . 
                                name = cdl.show()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                key = LookupServiceList.ServiceList(name)#. . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                tester = List_Func(key)# . . . . . . . . . . . . . . . . . > list . . . > list . . . > list.  . . > list . . 
                                doubles_check = set(line.strip() for line in open(tester))# . . . . doubles. . . . . . . .
                                if file_name in doubles_check:#. . . . . . . Duplicate File Checher . . . . . . . . . . . . .
                                    dup = DuplicatedFile()# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                    dup.set_n(0)#. . . . . . Duplicate File Checher . . . . . . . . . . . . . . . . . . .
                                    dup()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                  
                                    client.send(MainReplies.ServerReplies(31))#. . . . . . . . . . . . . . . . . . . . 
                                    break#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                else:#___________________________________________. . . . . . . . . . . . . . . . . . . . .
                                    client.send(MainReplies.ServerReplies(27))#. . . . . . . . . . . . . . . . . . . .
                                    data2 = client.recv(socket_size)#. . . . . . . . . . . . . . . . . . . . . . .
                                    if data2:#___________________. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                        exit_func = pound(data2)#. . . . Live Mic. . . . . . . . . . . . . . . . . . . . .
                                        if exit_func == 1:#_______________________________. . . . Live Mic. . . . . . .
                                            client.send(MainReplies.ServerReplies(31))#. . . . . . . . . . . . . . . .
                                            inv = Identifiers.Invalid()#. . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                            inv.set_n(1)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . 
                                            inv()#. . . . . . . . . Live Mic. . . . . . .. . . . Live Mic. . . . . . .
                                            break#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                        else:#_____________________. . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                            file = (data2.decode())#. . . . . . . .  . . . . . . . . . . . . . . . . . .
                                            de = file#_______________. . . . . . . . . . . . . . . . . . . . . . . . . . 
                                            packet = DecodeServer(de)#. . . . . .. . .. . . . . . . . Live Mic. . . . . . .
                                            recording_time = (packet.decode())#. . . . . . . . . . . . . . . . . . . . . 
                                            check_integer = recording_time.isdigit()#. . . . . . . . . . . . . .
                                            if check_integer == True:#. . . . . . . . . . . . . . . . . . . . . . . . . .
                                                pass#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                                            else:#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                                client.send(MainReplies.ServerReplies(31))#. . . . . . . . . . . . . . . .
                                                inv = Identifiers.Invalid()#. . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                                inv.set_n(1)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . 
                                                inv()#. . . . . . . . . Live Mic. . . . . . .. . . . Live Mic. . . . . . .
                                                break#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                            file_time = int(recording_time)# . . . . . . . . . . . . . . . . . . . . . . 
                                            if file_time >= 3 and file_time <= 900:#. . . . Live Mic. . . . . . . . . . .
                                                print('> recording time pass')#_____________. . . . . . . . . . . . . . .
                                                client.send(MainReplies.ServerReplies(26))#. . . . Live Mic. . . . . .
                                                root_dir = cdl.show()# . . . . . . . . . . . . . . . . . . . . . . . . .
                                                self = root_dir# . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                                depack = file_name# . . . . . . . .  . . . . . . . . . . . . . . . . . .
                                                if recorder_lock == 1:# . . . . . . . . . . . . . . . . . . . . . . . . .
                                                    wsf = WriteServiceFile(self + depack)#. . . . . . . . . . . . . . . . . .
                                                key = LookupServiceList.ServiceList(self)#. . . . . . . . . . . . . . . .
                                                dirlk = DirectoryLookup_Func(key)# . . . . . . . . . . . . . . . . . . .
                                                dirslt = ServiceDirectory_Func(key)#.      List File Service  list list list dir
                                                if recorder_lock == 1:#. . . . . . . . . . . . . . . . . . . . . . . . . .
                                                    wsl = WriteServiceList(dirslt, depack)#. . . . . . . . . . . . . . . . .
                                                    wsi = WriteSoundInfo(dirslt, depack, file_time) 
                                                cc = Open_Mic(root_dir, file_name, file_time, recorder_lock)# . . . . . . . .
                                                client.send(MainReplies.ServerReplies(28))# . . . . . . . . . . . . . 
                                                break# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                            else:#____________________________________________ . . . . . . . . . . . . . 
                                                client.send(MainReplies.ServerReplies(31))#Pound . . . . .ound .
                                                inv = Identifiers.Invalid()#. . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                                inv.set_n(1)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . 
                                                inv()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                                                break#___________________________________________________________________
                    elif dic == 24:#Server*Stream . . . . . . . Server*Stream . . . . . . . Server*Stream 
                        dk.set_n(0)#__________________________________Server*Stream . . . . . . . Server*Stream 
                        client.send(MainReplies.ServerReplies(29))#. . . . . . . Server*Stream . .. . Server*Stream 
                        recorder_lock = 1#. . . . Server*Stream . . . . . . . Server*Stream . . . . . . . Server*Stream 
                    elif dic == 25:#__________Recorder OFF  . . . . . . . . . . . .Recorder OFF___________________________
                        dk.set_n(0)#_________________________________Recorder OFF  . . . . . . . . . . . .Recorder OFF 
                        client.send(MainReplies.ServerReplies(30))#Recorder OFF  . . . . . . . . . . . .Recorder OFF 
                        recorder_lock = 0# . . . . . . . Recorder OFF . . . . .  Recorder OFF  Recorder OFF                   
                    elif dic == 26:# . Soundlist . . . Soundlist . . Soundlist . . . .Soundlist . . . Soundlist 
                        dk.set_n(0)#. . . . . . . . . Soundlist. . . . . . .Soundlist . . . Soundlist . . Soundlist 
                        file1 = ''#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        slf = Soundlist(file1)#. . . . . . . . . . . Soundlist . . . Soundlist . . Soundlist . . . . . .
                        en = (slf.decode())#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        codec = EncodeServer(en)#. . . . . . . .  . . . . . . . .  .Soundlist. . . Soundlist .. . . 
                        client.send(codec)#. . . . . . . . . . . . . . Soundlist . . . Soundlist . . Soundlist 
                    else:#____________________________________________
                        client.send(MainReplies.ServerReplies(10))#. . . . . . . . . . . . . . . . . . . . . . . . . .
                        inv = Identifiers.Invalid()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        inv.set_n(1)#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        inv()#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                    print('________________________')# . . . . . . . .
                    enter = Identifiers.EnterRec()#. . . . . . . 
                    enter.set_n(0)#. . . . . . . . . . . . . . .
#                    enter()#. . . . . . . . . . . . . . . . . .
                    td = Identifiers.TimeDate()# . . . . . . . . 
                    td.set_n(0)#. . . . . . . . . . . . . . . . .
#                    td()#. . . . . . . . . . . . . . . . . . .
                    addr = Identifiers.AddRec()#. . . . . . . . .
                    addr.set_n(0)#. . . . . . . . . . . . . . . .
#                    addr()#. . . . . . . . . . . . . . . . . . . . . . .
                    lur = Identifiers.LookupRec()#. . . . . . . . . .
                    lur.set_n(0)#. . . . . . . . . . . . . . . . . .
#                    lur()#. . . . . . . . . . . . . . . . . . . . .
                    ulr = Identifiers.UploadRec()#. . . . . . . . .
                    ulr.set_n(0)#. . . . . . . . . . . . . . . . . .
#                    ulr()#. . . . . . . . . . . . . . . . . . . . .
                    dlrc = Identifiers.DownloadRec()#. . . . . . . . .
                    dlrc.set_n(0)#. . . . . . . . . . . . . . . . . . .
#                    dlrc()#. . . . . . . . . . . . . . . . . . . . . .
                    ltr = Identifiers.ListRec()#. . . . . . . . . . . . . .
                    ltr.set_n(0)#. . . . . . . . . . . . . . .
#                    ltr()#. . . . . . . . . . . . . . . . . .
                    md = Identifiers.DirList()#. . . . . .
                    md.set_n(0)#. . . . . . . . . . . . . . . . . .
#                    md()#. . . . . . . . . . . . . . . . . . . .
                    dc = Identifiers.DirChange()#. . . . . .
                    dc.set_n(0)#. . . . . . . . . . . . . . . . . .
#                    dc()#. . . . . . . . . . . . . . . . . . . .
                    mdy = Identifiers.MakeDirectory()#... ..
                    mdy.set_n(0)#. . . . . . . . . . . . . . . .
#                    mdy()#. . . . . . . . . . . . . . . . . . . . .
                    pcd = Identifiers.Pics_Codec()#. . . . .
                    pcd.set_n(0)#. . . . . . . . . . . . . . . . . .
#                    pcd()#. . . . . . . . . . . . . . . . . . .
                    mod001 = Identifiers.ModuleLoader()#. . . . .
                    mod001.set_n(0)#. . . . . . . . . . . . . . . .
#                    mod001()#. . . . . . . . . . . . . . . . .
                    dylls= DireectoryList()#. . . . . . . .
                    dylls.set_n(0)#. . . . . . . . . . . . . . . 
#                    dylls()#. . . . . . . . . . . . . . . . . . 
                    dup = DuplicatedFile()# . . . . . . . . . .
                    dup.set_n(0)# . . . . . . . . . . . . . . . . 
#                    dup()#. . . . . . . . . .. . . . . . . . . .
                    inv = Identifiers.Invalid()#######
                    inv.set_n(0)##########
#                    inv()#################
                    extr = Identifiers.ExitRec()######
                    extr.set_n(0)#########
#                    extr()################
            except:#_______________________________
                print('> Client Disconnected <')#
                client.close()#
                return False#
#____________________
sdt  = SysDateTime()#_______________________
print('Server Started. ', sdt.currentdate())#
if __name__ == "__main__":#_______________________
    ThreadedServer(ipser, 12346).listen()#
