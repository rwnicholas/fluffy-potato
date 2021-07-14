#!/usr/bin/python3.8

import socket

HOST = '127.0.0.1'
PORT = 3940

teste = '123.049.604-13'

def valida_cpf(cpf):
    cpf = str(cpf)
    sum_1 = 0
    sum_2 = 0

    if len(cpf) != 11 and not cpf.isdecimal():
        print('eita')
        return "CPF Inválido!"
    
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
    
    if dig_1 == int(cpf[9] and dig_2 == int(cpf[10])):
        print("ihuuuuu")
    else:
        print("viiiiiiiiiish")
    

valida_cpf('52998224725')

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
#     soc.bind((HOST, PORT))
#     soc.listen()
#     conn, addr = soc.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)