# -*- coding: utf-8 -*-

import socket
import numpy as np
import threading
import cv2

host = "0.0.0.0"
port = 10001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print "[*] Listening on %s:%d" % (host, port)

def handle_client(client_socket):
    #request = client_socket.recv(1024)
    #print request

    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()

    quality = 100
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    jpgstring = cv2.imencode('.jpeg', frame, encode_param)[1].tostring()

    client_socket.send(jpgstring)

    client_socket.close()

while True:
    client, addr = server.accept()

    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
