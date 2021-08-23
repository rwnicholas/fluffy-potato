#!/usr/bin/python3

import socket, pickle

HOST = '127.0.0.1'
PORT = 39400

def send_to():
    data = {
        "type": "lookup",
        "nome": None,
        "atr_operacao": None,
        "atr_entrada": None,
        "atr_entrada_type": None
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((HOST, PORT))
        soc.sendall(pickle.dumps(data))

        response = soc.recv(1024)
        
        print(pickle.loads(response))

send_to()