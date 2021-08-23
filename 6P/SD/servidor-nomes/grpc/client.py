#!/usr/bin/python3
import grpc

import produto_pb2_grpc, produto_pb2

channel = grpc.insecure_channel('localhost:3940')
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

