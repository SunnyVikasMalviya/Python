import sys
import socket
from _thread import *

host = ''
port = 5555   #5555 is the port number for localhost server for your computer.
#What we do here is, we create a socket and bind it to the port 5555. For that\
#we have to open the port 5555 of our system using command prompt. After the \
#connection is established, we are just printing the connection details and not\
#really listening or responding to any request.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    s.bind((host, port))   #We bind the socket to the port
except socket.error as e :
    print(str(e))

#The line below listens to the port 5555 and acts as a queue and allows only 5\
#incoming connections at a time and rejects any more than that to avoid slower\
#connections.
s.listen(5)
print('Waiting for a connection.')
def threaded_client(conn) :
    conn.send(str.encode('Welcome, type your information\n'))

    while True :
        data = conn.recv(2048)
        reply = 'Server output : '+data.decode('utf-8')
        if not data :
            break
        conn.sendall(str.encode(reply))
    conn.close()

while True :
    conn, addr = s.accept()
    print('connected to: '+addr[0]+':'+str(addr[1]))

    start_new_thread(threaded_client, (conn, ))
'''
Steps to obtain the output:
1. Run this program
2. Go to Command Prompt
3. Type 'telnet localhost 5555' and enter
4. Output appears on the python shell
'''
'''
OUTPUT
connected to: 127.0.0.1:51203
'''

