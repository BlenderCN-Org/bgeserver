#!/usr/bin/env python
#/ Last Backup / 2017 / Feb / 09 / Current Projects / ThreadingServer101.py
#/ Module / Import / LookupServiceList.py
def ServiceList(listing_key):#
    listing = {
            'C:/Projects/Projects/'        :0,                                            
            'C:/Projects/ServerAddmin/'    :1,
            'C:/Projects/ServerDirectory/' :2,  
            'C:/Projects/ServerFiles/'     :3,
            'C:/Projects/ServerPics/'      :4,
            'C:/Projects/ServerSound/'     :5,
            'C:/Projects/gstar/'           :6,
            'C:/Projects/Modules/'         :7,
    }
    return listing[listing_key]#
#name = 'C:/Projects/Projects/'
#LookupServiceList.ServiceList(name)
#print(name)
