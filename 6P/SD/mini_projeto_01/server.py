#!/usr/bin/python3
import grpc
from concurrent import futures
import time

import produto_pb2, produto_pb2_grpc

import aracity

class AracityServicer(produto_pb2_grpc.Produto_EntregueServicer):
    def EntregaProduto(self, request, context):
        response = produto_pb2.Resposta()
        response.resposta = aracity.entrega_produto(request.produto, request.data_entrega, request.status)

        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=15))

produto_pb2_grpc.add_Produto_EntregueServicer_to_server(
    AracityServicer(), server
)
print('Ouvindo a porta 3940.')
server.add_insecure_port('[::]:3940')
server.start()

try:
    while True:
        time.sleep(39400)
except KeyboardInterrupt:
    server.stop(0)