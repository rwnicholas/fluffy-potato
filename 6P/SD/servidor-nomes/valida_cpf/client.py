#!/usr/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 39400

cpf = '52998224725'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.connect((HOST, PORT))
    soc.sendall(cpf.encode())

    data = soc.recv(1024)
    print(data.decode())