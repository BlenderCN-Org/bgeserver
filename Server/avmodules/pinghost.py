bit = 0
def OnlineCheck(bit):
    import os
    bit = 0
    hostname = "192.168.2.16" #example
    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
      print( hostname, 'is up!')
      bit = 1 
    else:
      print (hostname, 'is down!')
      bit = 1
      return bit
