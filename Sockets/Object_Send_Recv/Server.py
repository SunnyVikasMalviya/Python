#Objective : How to send and receive objects/ files/ anything(literally).
import socket
import time
import pickle

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((socket.gethostname(), 1236))
ss.listen(5)

HEADERSIZE = 10

while True:
    clientsocket, address = ss.accept()
    print(f"Connection from {address} has been established!")

    d = {1: "Hey", 2: "There", 3: "Gareeb"}
    #This is our object
    msg = pickle.dumps(d)
    #This is our message in bytes
    #We can send any object/ files etc. in bytes using pickle.
    #Pickling our object i.e. from object to bytes.
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    #Here we add the len(msg) as the header(in bytes) to the message.
    clientsocket.send(msg)
    #clientsocket.close()               #No need of this anymore.
    
'''
HOW TO RUN

1. Go to the folder where both the Server.py and the Client.py files are kept.
2. On the location bar, type cmd; command prompt will open up.
3. Type py Server.py in cmd pmt.
4. Do step 1 and 2 agian and this time type py Client.py in cmd pmt.
5. See the output has appeared in both the cmd pmt screens.
'''
