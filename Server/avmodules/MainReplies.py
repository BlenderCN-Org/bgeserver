#!/usr/bin/env python
#/ Last Backup / 2017 / Feb / 04 / Current Projects / ThreadingServer101.py
#/ Module / Dictionary / Import / MainReplies.py
def ServerReplies(replies_key):#IyMjLSMjIy0jIyMj
    replies = {
        0: b'IyMjLSMjIy0jIyMj',
        1: b'PiBHc3RhciBuZXQgPA==',
        2: b'TWFpbiBNZW51ID4gfCBzZXJ2aWNlbGlzdC4gIHwgbGlzdC4gfCBkaXIuIHwgc2hvdyBsaXN0LiB8IHNob3cgZGlyLiB8IGxpc3QvZGlyLg==',
        3: b'QWRkbWluIHVwbG9hZCBkaXJlY3RvcmllcyBwbGVhc2Uh',
        4: b'RGlyZWN0b3J5IHNhdmVkIHRvIFNlcnZlci4=',
        5: b'Pi4uLkZpbGUgTGFiZWxfX19uYW1lLio=',
        6: b'PlJlYWR5IGZvciBVcGxvYWQgOi8v',
        7: b'VGhhbmstWW91ISA+IGZyb20gOiAvR3N0YXIubmV0Lw==',
        8: b'Pi4uLkZpbGUgTGFiZWxfX19uYW1lLio=',
        9: b'Q2hhbmdlIERpcmVjdG9yeQ==',
        10: b'PiBJbnZhbGlkIFNlbGVjdGlvbiA8',
        11: b'RGlyZWN0b3J5IGhhcyBiZWVuIGNoYW5nZWQu',
        12: b'KF9fX19fX19fX18p', 
        13: b'QWRkbWluIEVudHJpZXMgOiBNYWtlIG5ldyBmb2xkZXIu',
        14: b'Rm9sZGVyIENyZWF0ZWQgLg==',
        15: b'U3lzdGVtIGxvY2tlZC4=',
        16: b'Q2FuY2VsIGVudHJ5',
        17: b'QWRkbWluIERpcmVjdG9yeSBMb2FkZXIu',
        18: b'PCBNb2R1bGUgbG9hZCA+',
        19: b'U2VydmVyIGxpc3RpbmcgbW9kdWxlcy4=',
        20: b'PiBFbnRlciBmaWxlIHNpemUgKiA+',
        21: b'UmVxdWVzdCBmaWxlIHNpemUgTGFiZWwgKg==',
        22: b'Q29kZWMgUmVhZHku',
        23: b'U2VydmVyIG5hbWUgOi8vZ3N0YXIubmV0LzEwMQ==',
        24: b'RHVwbGljYXRlIGZpbGUgTGFiZWwgLio=',
        25: b'Pj4+ICogTGl2ZSBNaWMgKiA+IEZpbGUgOiBMYWJlbC53YXY=',
        26: b'UmVjb3JkaW5nICogKiAqICogKg==',
        27: b'Pj4+ICogKiBFbnRlciB0aW1lIGZvciBSZWNvcmRpbmcgLiAqICo=',
        28: b'Pj4+ICogRmluaXNoZWQgUmVjb3JkaW5nICogPDw8PA==',
        29: b'PiogU3RyZWFtIFNlcnZlciAqPA==',
        30: b'PiAqIFJlY29yZGVyIE9GRiAqIDw=',
        31: b'Iw==',
        32: b'cGxheSB3YXZl',
        33: b'cG9wdXA=',
    }
    return replies[replies_key]#
#
def dict_ServerReplies():#_.........
    import Endeserver#####
    dict_list = []#
    print('> dict_ServerReplies <')#
    for k in range(33):#_____________________________
        list_pack = (ServerReplies(k))#
        dict_list.append(list_pack) #     
    for k in dict_list:#
        de = (k.decode())#
        unpack = Endeserver.DecodeServer(de)#
        print(unpack.decode())#
