# cient.py
import socket
import sys

if(len(sys.argv) < 3):
    print 'Usage : python client.py hostname port'
    sys.exit()

host = sys.argv[1]
port = int(sys.argv[2])

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
tm = s.recv(1024)

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))
