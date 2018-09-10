#!/usr/bin/env python
#/ Last Backup / 2017 / Feb / 04 / Current Projects / ThreadingServer101.py
#/ Module / Dictionary / Import / SearchDirect.py
def DirectoryFinder(listing_key):#
    listing = {
        0: 'C:/Projects/Projects/'          ,
        1: 'C:/Projects/ServerAddmin/'      ,
        2: 'C:/Projects/ServerDirectory/'   ,
        3: 'C:/Projects/ServerFiles/'       ,
        4: 'C:/Projects/ServerPics/'        ,
        5: 'C:/Projects/ServerSound/'       ,
        6: 'C:/Projects/gstar/'             ,
        7: 'C:/Projects/Modules/'           ,
    }
    return listing[listing_key]#
##name = SearchDirect.DirectoryFinder(6)
##print(name)
def dict_SearchDirect():#_.........
    import LookupServiceList##
    print('> dict_SearchDirect plus dict_LookupServiceList <')#
    for k in range(8):#_____________________
        list_pack = (DirectoryFinder(k))#
        print('> SearchDirect plus LookupServiceList Keys* ',LookupServiceList.ServiceList(list_pack))#
        print(list_pack)#
