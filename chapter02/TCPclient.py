# -*- coding: utf-8 -*-

import socket

#target_host = "www.google.com"
#target_port = 80

target_host = "192.168.11.39"
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

#client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

client.send(b"GET / HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n")

response = client.recv(4096)

print response
