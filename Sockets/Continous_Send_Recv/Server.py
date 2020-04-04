#Objective : How to handle socket connection without closing server connection.
import socket
import time

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((socket.gethostname(), 1236))
ss.listen(5)

HEADERSIZE = 10
#A header will be added to all our messages which will contain the length of the
#message, to notify the client how long is the message. Here 10 means that the
#header added in front of the message is of length 10, which means the size of
#message can be max 9,999,999,999 characters/bytes long.

while True:
    clientsocket, address = ss.accept()
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    #This is our message
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    #Here we add the len(msg) as the header to the message
    clientsocket.send(bytes(msg, "utf-8"))
    #clientsocket.close()               #No need of this anymore.
    #Now we are continously going to send the current time to the client.
    #This will act as a unclosed connection.
    while True:
        time.sleep(3)
        #Every 3 seconds we send the current time.
        msg = f"The time is : {time.time()}"
        #This is our message
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        #Here we add the len(msg) as the header to the message
        clientsocket.send(bytes(msg, "utf-8"))
    
'''
HOW TO RUN

1. Go to the folder where both the Server.py and the Client.py files are kept.
2. On the location bar, type cmd; command prompt will open up.
3. Type py Server.py in cmd pmt.
4. Do step 1 and 2 agian and this time type py Client.py in cmd pmt.
5. See the output has appeared in both the cmd pmt screens.
'''
