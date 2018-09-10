#/usr/bin/env python
#/Last update / 2017 / Feb / 21 / Current Projects / AddminClient.py 
#/Addminfunc.py
#/Command Addmin Console 
#/Reference /scroll = ('down/', 'up/', 'bin/', 'live mic', 'raw/', 'exit')

def addmin_console(name, key):#___________________________________________________________________________________________________
    def func0(key):#_________________
        print ('> * down/ * >')#
        key = 0 #
        return key#___________________

    def func1(key):#_________________
        print ('> * up/ * >')#
        key = 1# 
        return key#___________________

    def func2(key):#_________________
        print ('> * bin/ * >')#
        key = 2# 
        return key#___________________

    def func3(key):#_________________
        print ('> * Live Mic * >')#
        key = 3# 
        return key#___________________

    def func4(key):#_________________
        print ('> * raw/ * >')#
        key = 4# 
        return key#___________________

    def func5(key):#_________________
        print ('> * exit * >')#
        key = 5# 
        return key#___________________

    menu = {'down/'         : func0,
            'up/'           : func1,
            'bin/'          : func2,
            'live mic'      : func3,
            'raw/'          : func4,
            'exit'          : func5,
            }#______
    functocall = menu[name]#
    key = functocall(key)#___________('down/', 'up/', 'bin/', 'live mic', 'raw/', 'exit')
    return key#

##for item in scroll:
##    key = 0
##    name = item
##    fm = addmin_console(name, key)
##    key = fm
##    
##    print(key)
##


##num = ('1' , '2', '3', '4', '5', '6', '7', '8', '9', '0')
##lbl = label()
##lbs = size()
##def make_label(label):
##    label = input('* record label *')
##    lbl.set_n(label)
##    return label
##def make_size(size):
##    size = input('* record size *')
##    lbs.set_n(size)
##    return size
##
##def redo_label(label):
##    label = input('* redo label *')
##    return label
##def redo_size(size):
##    size = input('* redo size *')
##    return size
##
##
##make_label(label)
##exten = lbl.get_n()
##exten_cont = len(exten)    
##if exten[-4:exten_cont] == '.wav':
##    print('label pass')
##    pass
##else:
##    rl = redo_label(label)
##    rerl = len(rl)
##    if rl[-4:rerl] == '.wav':
##        print('label pass')
##        pass
##    else:
##        print('Invalid')
##
##
##make_size(size)
##if lbs.get_n() in num: 
##    print('size pass')
##    pass
##else:
##    rd = redo_size(size)
##    if rd in num:
##        print('size pass')
##        pass
##    else:
##        print('Invalid')
##
##print('Record file ',lbl.get_n(), lbs.get_n())
##
        







    












