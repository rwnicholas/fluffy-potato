#!/usr/bin/python3

import pickle
import socket

cpf = '52998224725'

def lookup():
    HOST = '127.0.0.1'
    PORT = 39400
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        data = {
            "type": "lookup",
            "nome": "valida_cpf",
            "atr_operacao": None,
            "atr_entrada": None,
            "atr_entrada_type": None
        }
        soc.connect((HOST, PORT))
        soc.sendall(pickle.dumps(data))

        response = soc.recv(1024)
        msg = pickle.loads(response)
        print(msg)

        return msg

try:
    addr = lookup()[0]['addr']
    print("Referência de servidor encontrada no endereço:", addr)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect(addr)
        soc.sendall(cpf.encode('utf-8'))

        response = soc.recv(1024)
        print(response.decode('utf-8'))
except:
    print("Servidor não encontrado")