#/usr/bin/env python
#/ Last update / Mar / 23 / 2017 / Current Projects / live_mic.py
import pyaudio######
import socket#
import socketdatetime#
sdt = socketdatetime.SysDateTime()#
CHUNK = 1024#
FORMAT = pyaudio.paInt16# . Stream Live . . . . . . . . . . . Stream Live
CHANNELS = 1#
RATE = 44100#
clock_now = socketdatetime.sdt.clocktime()#
HOST = '192.168.2.23'    # The remote host
PORT = 12367 #    :        # The same port as used by the server
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
    sdt = socketdatetime.SysDateTime()#
    time_string = (socketdatetime.sdt.clocktime())#
    if str(time_string) == str(b.time()):#
        print('> Mic OFF ', socketdatetime.sdt.clocktime())# . . . Live Mic. . .
        break#
stream.stop_stream()#
stream.close()#
p.terminate()#
s.close()#

