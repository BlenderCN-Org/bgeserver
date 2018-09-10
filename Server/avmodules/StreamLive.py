#/usr/bin/env python
from socket import socket, AF_INET, SOCK_STREAM#
import datetime####
import base64#######
import time#####
import pyaudio######
from base64 import decodestring#
class SysDateTime(object):#
    def __init__(self):#______________________
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



class Connection:#_________________________________________________
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):#
        self.directoryPrint = []#
        self.file_download = {}#
        self.address = address#
        self.family = AF_INET#
        self.type = SOCK_STREAM#
        self.sock = None#

    def __enter__(self):#
        if self.sock is not None:#
            raise RuntimeError('< Already Connected >')#
        self.sock = socket(self.family, self.type)#
        self.sock.connect(self.address)#
        self.sock.settimeout(None)#
        print('< CONNECTED >')#
        return self.sock#

 #######################
    def __exit__(self):#, exc_ty, exc_val, tb):_______________________
        print('Module closed')
        self.sock.close()#

    def __Stream_Live__(self):
        import socket#
        print('Stream_Live_Module. created Setp 11, 2017')
        while True:#____________ . . . . . . . . . Stream Live . . . . . . . . . . . Stream Live
#            name = name.strip()#
            requestHeader = ('> Stream Live .')#
            header = requestHeader#
            print(header)#
            name = ('live mic')
            code = name.encode('ascii', 'ignore')#
            binary = base64.b64encode(code)#
            self.sock.send(binary)#
            data = self.sock.recv(1024)#
            if data:#________________________________________
                self.file_download = (base64.b64decode(data))#
                print(self.file_download.decode())#
                name = input('< File Label . * > ')#
                name = name.strip()#
                code = name.encode('ascii', 'ignore')# . Stream Live . . . . . . . . . . . Stream Live
                binary = base64.b64encode(code)#
                self.sock.send(binary)#
                data = self.sock.recv(1024)#
                if data:#_________________________________________
                    self.file_download = (base64.b64decode(data))#
                    print(self.file_download.decode())#
                    check_limit = self.file_download.decode()#
                    if check_limit == ('#'):#
                        print('> Duplicated Label <')#
                        break#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                    sdt = SysDateTime()#
                    rec_time = input('> recording time < ')#
                    rec_time = rec_time.strip()#
                    check_integer = rec_time.isdigit()# . Stream Live . . . . . . . . . . . Stream Live
                    if check_integer == True:#
                        print('> pass')#
                    else:#
                        print('> fail')#
                        name = '#'#
                        code = name.encode('ascii', 'ignore')#
                        binary = base64.b64encode(code)#
                        self.sock.send(binary)#
                        data = self.sock.recv(1024)#
                        if data:#______________________
                            self.file_download = (base64.b64decode(data))#
                            print(self.file_download.decode())#
                            break#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                    code = rec_time.encode('ascii', 'ignore')#
                    binary = base64.b64encode(code)#
                    self.sock.send(binary)#
                    data = self.sock.recv(1024)#
                    if data:#_________________________________________
                        self.file_download = (base64.b64decode(data))# . Stream Live . . . . . . . Stream Live
                        print(self.file_download.decode())#
                        check_limit = self.file_download.decode()#
                        if check_limit == ('#'):#
                            print('> Invalid time, > 3 sec. < 900 sec.')#
                            break#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        else:#_________________
                            sdt = SysDateTime()#
                            a = datetime.datetime(100,1,1,int(sdt.currenthour()),int(sdt.currentminut()),int(sdt.currentsec()))
                            b = a + datetime.timedelta(0,int(rec_time))# days, seconds, then other fields.
                            self.file_download = (base64.b64decode(data))#
                            print(self.file_download.decode())#
                            CHUNK = 1024#
                            FORMAT = pyaudio.paInt16# . Stream Live . . . . . . . . . . . Stream Live
                            CHANNELS = 1#
                            RATE = 44100#
                            clock_now = sdt.clocktime()#
                            HOST = '192.168.2.16'    # The remote host
                            PORT = 1236 #    :        # The same port as used by the server
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#
                            s.connect((HOST, PORT))#
                            p = pyaudio.PyAudio()#
                            stream = p.open(format = FORMAT,
                                            channels = CHANNELS,
                                            rate = RATE,
                                            input = True,
                                            frames_per_buffer=CHUNK)# . Stream Live . . . . .. . . Stream Live
    #                                        notify = sdt.currentsec()#
                            for i in range(0, int(RATE/CHUNK*int(rec_time))):#
                                data  = stream.read(CHUNK)#
                                s.sendall(data)#
                                sdt = SysDateTime()#
                                time_string = (sdt.clocktime())#
                                if str(time_string) == str(b.time()):#
                                    print('> Mic OFF ', sdt.clocktime())# . . . Live Mic. . .
                                    break#
                            stream.stop_stream()#
                            stream.close()#
                            p.terminate()#
                            s.close()#
                        data = self.sock.recv(1024)# . Stream Live . . . . . . . . . . . Stream Live
                        if data:#______________________
                            self.file_download = (base64.b64decode(data))#
                            print(self.file_download.decode())#
                            break#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                        else:#_____________________________________________________
                            print('< Incorrect padding > ', data)#
                            break#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    #___________________________
if __name__ == '__main__':#
    print('> Client Server REC. <')#________________
    player1 = Connection(("192.168.2.16",12345))#
    player1.__enter__()#
    player1.__Stream_Live__()#
    player1.__exit__()#
