import socket
import select
import errno
import sys

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

my_username = input("Username: ")
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect((IP, PORT))
cs.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
cs.send(username_header + username)

while True:
    message = input(f"{my_username} > ")

    if message:
        message = message.encode("utf-8")
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
        cs.send(message_header + message)

    try:
        while True:
            # receive things
            username_header = cs.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Connection closed by the server")
                sys.exit()

            username_length = int(username_header.decode("utf-8").strip())
            username = cs.recv(username_length).decode("utf-8")

            message_header = cs.recv(HEADER_LENGTH)
            message_length = int(message_header.decode("utf-8".strip()))
            message = cs.recv(message_length).decode("utf-8")

            print(f"{username} > {message}")
            

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error', str(e))
            sys.exit()
        continue

    except Exception as e:
        print('General error', str(e))
        sys.exit()
