# -*- coding: utf-8 -*-

import socket

target_host = "127.0.0.1"
#target_host = "www.google.com"
#target_port = 80
target_port = 4000

# make socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client.connect((target_host, target_port))

# send data
#client.send("GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")
client.send("Hello!")

# receive data
response = client.recv(4096)

print response