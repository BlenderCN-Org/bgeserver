#!/usr/bin/env python
#/ Last Backup / 2017 / Mar / 01 / Current Projects / ThreadingServer101.py
#/ Module / Dictionary / Import / MainRequest.py
def ServerRequest(request_key):#
    request = {
        0: b'IyMjLSMjIy0jIyMj',
        1: b'Z3N0YXI=',
        2: b'dGltZQ==',
        3: b'MS5hZGQ=',
        4: b'ZGly',
        5: b'dXBsb2Fk',
        6: b'ZG93bmxvYWQ=',
        7: b'c2hvdyBsaXN0',
        8: b'Y2Qv',
        9: b'bWVudQ==',
        10: b'c2VydmVyIG5hbWU=',
        11: b'c2hvdyBkaXI=',
        12: b'YWRkbWluL2Rpci9nc3Rhcg==',
        13: b'MTY0NS5iYWRhc3Mvc2VydmVyL2ZvcmV2ZXI=',
        14: b'TG9hZCBpbiBTZXJ2ZXIgRGlyZWN0b3JpZXMu',
        15: b'bGlzdA==',
        16: b'c2VydmVybGlzdA==',
        17: b'bW9kdWxl',
        18: b'c3lzdGVtIG1vZHM=',                       
        19: b'c2Vydm5hbWU=',
        20: b'c29ja2V0IHNpemU=',
        21: b'Z2V0IGZpbGUgc2l6ZQ==',
        22: b'c2V0IGNvZGVj',
        23: b'bGl2ZSBtaWM=',
        24: b'c2VydmVyKnN0cmVhbQ==',
        25: b'cmVjb3JkZXIgb2Zm',
        26: b'c291bmRsaXN0',
        27: b'Iw==',
        28: b'cGxheSB3YXZl',
        29: b'cG9wdXA=',
    }
    return request[request_key]#
#
def dict_ServerRequest():#.........
    import Endeserver#####
    dict_list = []#
    print('> dict_ServerRequest <')#
    for k in range(29):#_____________________________
        list_pack = (ServerRequest(k))#
        dict_list.append(list_pack) #     
    for k in dict_list:#
        de = (k.decode())#
        unpack = Endeserver.DecodeServer(de)#
        print(unpack.decode())#
