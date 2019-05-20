# -*- coding: utf-8 -*-

import socket
import numpy as np
import cv2

#host = "192.168.x.y"
host = "192.168.11.30"
port = 10001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

print ("[*] Listening on %s:%d" % (host, port))
#client.send(b"GET / HTTP/1.1\r\nHost: " + host + "\r\n\r\n")

capture = cv2.VideoCapture(0)
ret, frame = capture.read()

quality = 100
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
jpgstring = cv2.imencode('.jpg', frame, encode_param)[1].tostring()

client.send(jpgstring)

client.close()

print ("sent data")
