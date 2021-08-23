#!/usr/bin/python3
import grpc, socket, pickle

import produto_pb2_grpc, produto_pb2

def lookup():
    HOST = '127.0.0.1'
    PORT = 39400

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        data = {
            "type": "lookup",
            "nome": "entregar_produto",
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
    channel = grpc.insecure_channel(addr[0] + ':' +str(addr[1]))
    stub = produto_pb2_grpc.Produto_EntregueStub(channel)

    produto = input("Digite o produto: ")
    data_entrega = input("Digite a data de entrega: ")
    status = input("Qual o status da entrega? (SUCESSO | FALHA) ")

    if status != "SUCESSO" and status != "FALHA":
        print("Apenas SUCESSO e FALHA são aceitos como entrada válida!")
    else:
        entrega = produto_pb2.Produto(produto=produto, data_entrega=data_entrega, status=status)
        response = stub.EntregaProduto(entrega)
        print(response.resposta)
except:
    print("Servidor não encontrado")
