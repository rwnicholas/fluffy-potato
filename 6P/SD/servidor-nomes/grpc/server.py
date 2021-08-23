#!/usr/bin/python3
import grpc, socket, pickle
from concurrent import futures
import time

import produto_pb2, produto_pb2_grpc

import aracity

def bind():
    data = {
        "type": "bind",
        "nome": "entregar_produto",
        "addr": "(localhost, 8001)",
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


class AracityServicer(produto_pb2_grpc.Produto_EntregueServicer):
    def EntregaProduto(self, request, context):
        response = produto_pb2.Resposta()
        response.resposta = aracity.entrega_produto(request.produto, request.data_entrega, request.status)

        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=15))

produto_pb2_grpc.add_Produto_EntregueServicer_to_server(
    AracityServicer(), server
)
print('Ouvindo a porta 8001.')
server.add_insecure_port('[::]:8001')
server.start()

try:
    while True:
        time.sleep(39400)
except KeyboardInterrupt:
    server.stop(0)