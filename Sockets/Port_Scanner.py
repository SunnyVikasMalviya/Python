import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'google.com'

#Port Scanner : A port scanner scans through required servers ports and \
#returns the open ports, to which we can connect.

#pscan() takes a port number as argument and checks whether or not it is open.
def pscan(port) :
    try :
        s.connect((server), port)
        return True
    except :
        return False

#Calling pscan() with 1 through 30 port numbers as argument.
for port in range(1, 30) :
    if pscan(port) :
        print('Port',port,'is open.!!!!!!!!!!!!!!')
    else :
        print('Port',port,'is closed.')
print('Done')
