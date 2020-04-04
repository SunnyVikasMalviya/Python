import socket

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#a socket object has been created
cs.connect((socket.gethostname(), 1234))
#our client socket is connect to our localhost server with port number 1234
#This doesn't happen usually that client and server sockets are on the same machine
#It has been done to explain things in an easy manner

full_msg = ''
while True:
    msg = cs.recv(8)
    #We receive the acknowledgement message that was sent to us; 8 is the buffer
    #size that describes how large a data chunk can we accept at a time
    if len(msg)<=0:
        break
    full_msg += msg.decode('utf-8')
print(full_msg)
#We receive the message and decode it; since our encoding scheme was utf-8



'''
HOW TO RUN

1. Go to the folder where both the Server.py and the Client.py files are kept.
2. On the location bar, type cmd; command prompt will open up.
3. Type py Server.py in cmd pmt.
4. Do step 1 and 2 agian and this time type py Client.py in cmd pmt.
5. See the output has appeared in both the cmd pmt screens.
'''
