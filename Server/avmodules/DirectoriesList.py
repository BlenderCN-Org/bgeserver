#!/usr/bin/env python
#/ Last Backup / 2017 / Feb / 21/ Current Projects / ThreadingServer101.py
#/ Module / Import / DirectoriesList.py
def Listings(listing_key):#
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
#
def dict_DirectoriesList():#_.........
    print('> dict_DirectoriesList <')#
    for k in range(8):#_____________________
        list_pack = (Listings(k))#
        print(list_pack)#
