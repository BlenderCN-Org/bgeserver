#!/usr/bin/env python
#/ Last Backup / 2017 / Feb / 09/ Current Projects / ThreadingServer101.py
#/ Module / Import / ServiceDirectories.py
def DirectoryListings(listing_key):#
    listing = {
        0: 'C:/Projects/ServerFileList/projectslist/projectservice',
        1: 'C:/Projects/ServerFileList/addminlist/addminservice',
        2: 'C:/Projects/ServerFileList/directorylist/directoryservice',
        3: 'C:/Projects/ServerFileList/filelist/fileservice',
        4: 'C:/Projects/ServerFileList/piclist/picservice',
        5: 'C:/Projects/ServerFileList/soundlist/soundservice',
        6: 'C:/Projects/ServerFileList/gstarlist/gstarservice',
        7: 'C:/Projects/ServerFileList/moduleslist/moduleservice',
    }
    return listing[listing_key]#
##name = ServiceDirectories.DirectoryServiceListings(3)
##print(name)
def dict_ServiceDirectory():#_.........
    print('> dict_ServiceDirectory <')#
    for k in range(8):#_____________________
        list_pack = (DirectoryListings(k))#
        print(list_pack)#
