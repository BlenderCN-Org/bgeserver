def platform():#
    n = 0#
    def func():#
        print(n)# 
    def get_n():#
        return n#
    def set_n(item):#
        global n#
        n = item
    func.get_n = get_n#
    func.set_n = set_n#
    return func#
#pf = platform(()
#pf.set_n(1)
#pf()
class __packet__:#_____________________________________________________________________________________________________
    def __init__(self, pack):#
        self.items = []#
        self.__update(pack)#

    def update(self, pack):#
        self.items = pack#

    def show(self):#___________
        print(self.items)#
    __update = update# 
