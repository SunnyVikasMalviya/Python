import socket

#Sockets aid in communication between 2 entities
#For example, a client and a server are 2 entities and the client requests a \
#url. Servers have their ports open that they use to serve different kinds of \
#requests. So the client generates a socket that plugs into the port of the \
#server and help communicate the server and the client.

#port 80 is used by websites for serving https requests
#port 20 for ftp
#port 22 for ssh
#lower number ports are very specific
#higher number ports are general purpose ports that can be used for any function

#Creating a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET denotes the connection type that we want to use, here IPv4
#can use sock_dgram in place of SOCK_STREAM
#SOCK_STREAM allows us to have a tcp connection

print(s)
'''
This was the result:
<socket.socket fd=768, family=AddressFamily.AF_INET, \
type=SocketKind.SOCK_STREAM, proto=0>
'''

server = 'pythonprogramming.net'
port = 80   #We will act like a browesr
server_ip = socket.gethostbyname(server)  #Getting the ip address of our server.
#ping is a command used in prompt to get ip of the servers
print(server_ip)

#104.237.143.20

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"   #Forming our request

s.connect((server, port))      #Connecting our socket to the server's port
s.send(request.encode())       #Sending the request
result = s.recv(1024)          #Storing the result in a variable
#1024 is the band width in which the data from the server is sent to the client.

print(result)

file = open("socket_result.txt", "w")
file.write(str(result))
file.close()

'''
result was:
b'HTTP/1.1 301 Moved Permanently\r\nDate: Tue, 20 Nov 2018 14:53:44 GMT\r\nServer:
Apache/2.4.10 (Ubuntu)\r\nLocation: https://pythonprogramming.net/\r\nContent-Length:
325\r\nContent-Type: text/html; charset=iso-8859-1\r\n\r\n<!DOCTYPE HTML PUBLIC "-//
IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>301 Moved Permanently</title>\n</head>
<body>\n<h1>Moved Permanently</h1>\n<p>The document has moved <a href="https://
pythonprogramming.net/">here</a>.</p>\n<hr>\n<address>Apache/2.4.10 (Ubuntu) Server
at pythonprogramming.net Port 80</address>\n</body></html>\n'
'''
#The b at the start of the result denotes byte strings.

