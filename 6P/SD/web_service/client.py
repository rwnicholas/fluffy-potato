#!/usr/bin/python3

import requests

def menu():
    string_menu = "1- Obter lista de sucos\n2- Cadastrar novo suco\n3- Atualizar suco\n4- Deletar suco (id)\n5- Opções do servidor\n0- Sair\n"
    opt = int(input(string_menu))

    return opt

def get():
    response = requests.get("http://localhost:5000/api/")
    print("Resposta:", response.json())
    print("Status-code:", response.status_code)

def post(nome, litros):
    corpo = {
        "nome": nome,
        "litros": litros
    }

    response = requests.post("http://localhost:5000/api/", json=corpo)
    print("Resposta:", response.json())
    print("Status-code:", response.status_code)

def put(id, nome, litros):
    corpo = {
        "id": id,
        "nome": nome,
        "litros": litros
    }

    response = requests.put("http://localhost:5000/api/", json=corpo)
    print("Status-code:", response.status_code)

def delete(id):
    response = requests.delete("http://localhost:5000/api/", params={"id": id})
    print("Resposta:", response.content)
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
        n = input("Nome: ")
        l = float(input("Litros: "))
        post(n, l)

    elif opt == 3:
        i = int(input("Id: "))
        n = input("Nome: ")
        l = float(input("Litros: "))
        put(i, n, l)

    elif opt == 4:
        i = int(input("Id: "))
        delete(i)

    elif opt == 5:
        options()

    elif opt == 0:
        break