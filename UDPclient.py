# -*- coding: utf-8 -*-

import socket

#target_host = "0.0.0.0"
#target_port = 80 

target_host = "localhost"
target_port = 9999 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("data", (target_host, target_port)) 

data, addr = client.recvfrom(4096)

print data 
