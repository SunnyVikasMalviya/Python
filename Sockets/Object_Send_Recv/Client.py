import socket
import pickle

HEADERSIZE = 10

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect((socket.gethostname(), 1236))

while True:
    full_msg = b''          #The message is now in bytes...hence b.
    new_msg = True
    msg_len = 0
    while True:
        msg = cs.recv(16)
        if new_msg:
            msg_len = int(msg[:HEADERSIZE])
            print("New message length : {}".format(msg_len))
            new_msg = False

        full_msg += msg

        if len(full_msg)-HEADERSIZE == msg_len:
            print("Full message received.")
            print(full_msg[HEADERSIZE:])
            d = pickle.loads(full_msg[HEADERSIZE:])
            #Unpickling our object i.e. from bytes back to object.
            print(d)
            new_msg = True
            full_msg = b''
    

'''
HOW TO RUN

1. Go to the folder where both the Server.py and the Client.py files are kept.
2. On the location bar, type cmd; command prompt will open up.
3. Type py Server.py in cmd pmt.
4. Do step 1 and 2 agian and this time type py Client.py in cmd pmt.
5. See the output has appeared in both the cmd pmt screens.
'''
