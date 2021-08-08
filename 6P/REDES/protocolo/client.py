#!/usr/bin/python3

import socket, json

HOST = '127.0.0.1'
PORT = 39400

usuario = input("Login: ")

def send_to(send, read, content):
    data = {
        "send": send,
        "read": read,
        "content": content
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((HOST, PORT))
        soc.sendall(json.dumps(data).encode('utf-8'))

        response = soc.recv(1024)
        
        return json.loads(response.decode('utf-8'))

def menu():
    string_menu = "1- Ler mensagens\n2- Enviar mensagem\n3- Ler e enviar\n0- Sair\n"
    opt = int(input(string_menu))

    return opt

while True:
    opt = menu()

    if opt == 1:
        content = {
            "from": usuario,
            "to": None,
            "message": None
        }
        print(send_to(False, True, content))

    elif opt == 2:
        paraQuem = input("Para quem? ")
        mensagem = input("Qual a mensagem? ")

        content = {
            "from": usuario,
            "to": paraQuem,
            "message": mensagem
        }
        print(send_to(True, False, content))

    elif opt == 3:
        paraQuem = input("Para quem? ")
        mensagem = input("Qual a mensagem? ")

        content = {
            "from": usuario,
            "to": paraQuem,
            "message": mensagem
        }
        print(send_to(True, True, content))

    elif opt == 0:
        break


