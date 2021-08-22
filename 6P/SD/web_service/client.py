#!/usr/bin/python3

import requests

def menu():
    string_menu = "1- Obter lista de status dos produtos\n2- Cadastrar novo status de entrega\n3- Atualizar status de entrega\n4- Deletar status de entrega (id)\n5- Opções do servidor\n0- Sair\n"
    opt = int(input(string_menu))

    return opt

def get():
    response = requests.get("http://localhost:5000/api/")
    print("Resposta:", response.json())
    print("Status-code:", response.status_code)

def post(produto, data_entrega, status):
    corpo = {
        "produto": produto,
        "data_entrega": data_entrega,
        "status": status
    }

    response = requests.post("http://localhost:5000/api/", json=corpo)
    print("Resposta:", response.json())
    print("Status-code:", response.status_code)

def put(id, produto, data_entrega, status):
    corpo = {
        "id": id,
        "produto": produto,
        "data_entrega": data_entrega,
        "status": status
    }

    response = requests.put("http://localhost:5000/api/", json=corpo)
    print("Status-code:", response.status_code)

def delete(id):
    response = requests.delete("http://localhost:5000/api/", params={"id": id})
    print("Status-code:", response.status_code)

def options():
    response = requests.options("http://localhost:5000/api/")
    print("Headers:", response.headers)
    print("Status-code:", response.status_code)

while True:
    opt = menu()
    if opt == 1:
        get()

    elif opt == 2:
        p = input("Produto: ")
        d = input("Data entrega: ")
        s = input("Status da entrega (SUCESSO | FALHA): ")
        post(p, d, s)

    elif opt == 3:
        i = int(input("Id: "))
        p = input("Produto: ")
        d = input("Data entrega: ")
        s = input("Status da entrega (SUCESSO | FALHA): ")
        put(i, p, d, s)

    elif opt == 4:
        i = int(input("Id: "))
        delete(i)

    elif opt == 5:
        options()

    elif opt == 0:
        break