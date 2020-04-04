import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#a socket object has been created
#AF_INET corresponds to IPV4 and SOCK_STREAM corresponds to TCP
ss.bind((socket.gethostname(), 1234))
#the socket object is bond to the server and port number, for our case our
#localhost server and port number 1234
ss.listen(5)
#Keep listening for connection requests
#5 is the  queue length, 5 sockets can connect at a time

while True:
    clientsocket, address = ss.accept()
    #As soon as the request comes we accept the request
    #clientsocket is also a socket object same as ours but it denotes client
    #address is ipv4 address of the machine trying to connect to our server
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    #We send an acknowledgement message encoded in utf-8 encryption
    clientsocket.close()


'''
HOW TO RUN

1. Go to the folder where both the Server.py and the Client.py files are kept.
2. On the location bar, type cmd; command prompt will open up.
3. Type py Server.py in cmd pmt.
4. Do step 1 and 2 agian and this time type py Client.py in cmd pmt.
5. See the output has appeared in both the cmd pmt screens.
'''
