#/usr/bin/env python
#/Module/DirectoryRoot.py
# under construction not in use.
def DirectoryRoot(listing_key):#
    listing = {
        0: '',
        1: 'C:/gstar/ServerAddmin/'      ,
        2: 'C:/gstar/ServerDirectory/'   ,
        3: 'C:/gstar/ServerFiles/'       ,
        4: 'C:/gstar/ServerPics/'        ,
        5: 'C:/gstar/ServerSound/'       ,
        6: 'C:/gstar/gstar/'             ,
        7: 'C:/Projects/Projects/
    }
    return listing[listing_key]#
#
def DirectoryKey(listing_key):#
    listing = {
            'C:/gstar/ServerAddmin/'    : 1  ,
            'C:/gstar/ServerDirectory/' : 2  ,  
            'C:/gstar/ServerFiles/'     : 3  ,
            'C:/gstarServerPics/'       : 4  ,
            'C:/gstar/ServerSound/'     : 5  ,
            'C:/gstar/gstar/'           : 6  ,
    }
    return listing[listing_key]#

#file = DirectoryRoot(1)
#key = DirectoryKey(file)
#print(file, key)

