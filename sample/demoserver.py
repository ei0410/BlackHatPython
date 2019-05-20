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
    response = ''
    recvlen = 1

    while recvlen > 0:
        recvstr = client_socket.recv(1024)
        recvlen = len(recvstr)
        response += recvstr

    narray = np.fromstring(response, dtype="uint8")
    img = cv2.imdecode(narray, 1)
    cv2.imshow("Capture.jpg", img)
    cv2.waitKey(0)

    client_socket.send("ACK")

    client_socket.close()

while True:
    client, addr = server.accept()

    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
