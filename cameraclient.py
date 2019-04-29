# -*- coding: utf-8 -*-

import socket
import numpy
import cv2

#host = "192.168.x.y"
host = "192.168.11.2"
port = 10000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

client.send(b"GET / HTTP/1.1\r\nHost: " + host + "\r\n\r\n")

response = ''
recvlen = 100

while recvlen > 0:
    recvstr = client.recv(1024*8)
    recvlen = len(recvstr)
    response += recvstr

client.close()

narray = numpy.fromstring(response, dtype='uint8')

img = cv2.imdecode(narray, 1)

cv2.imshow('Capture.jpg', img)
cv2.waitKey(0)

#cv2.imwrite('Capture.jpg', img)
