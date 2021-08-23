#!/usr/bin/python3

import socket, pickle
import _thread

HOST = '127.0.0.1'
PORT = 8002

def bind():
    data = {
        "type": "bind",
        "nome": "valida_cpf",
        "addr": f"({HOST}, {PORT})",
        "atr_operacao": "validação",
        "atr_entrada": "cpf",
        "atr_entrada_type": "text"
    }
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect(('127.0.0.1', 39400))
        soc.sendall(pickle.dumps(data))

        response = soc.recv(1024)
        
        response = pickle.loads(response)
        print(response)

        if response['status'] == "ok":
            print("Endereço registrado no servidor de nomes")
            return True
        else:
            print("Não foi possível registrar no servidor de nomes")
            return False

def new_client(conn, addr):
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        mensagem = data.decode() + ": " + valida_cpf(data.decode())
        conn.sendall(mensagem.encode())
    conn.close()

def valida_cpf(cpf):
    cpf = str(cpf)
    sum_1 = 0
    sum_2 = 0

    if len(cpf) != 11 and not cpf.isdecimal():
        return "CPF Inválido! Apenas números são aceitos!"
    
    i = 0
    for x in range(10,1,-1):
        sum_1+= int(cpf[i])*x
        i+=1
    sum_1*=10

    i = 0
    for x in range(11,1,-1):
        sum_2+= int(cpf[i])*x
        i+=1
    sum_2*=10

    dig_1 = sum_1 % 11
    dig_2 = sum_2 % 11
    
    if dig_1 == int(cpf[9]) and dig_2 == int(cpf[10]):
        return "CPF Válido!!"
    else:
        return "CPF Inválido!"
if bind():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            _thread.start_new_thread(new_client, (conn, addr))