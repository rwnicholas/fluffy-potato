# Nomeação baseada em atributos
Para executar o sistema, lembrar de ter instalado o python3 e `grpcio`, `grpcio-tools`:
`pip install grpcio grpcio-tools`

### Execução Servidores:
`python .\servidor-nomes.py` executa o servidor de nomes.

`python .\grpc\server.py` executa o servidor grpc que informa aracity hardware que houve uma entrega.

`python .\valida_cpf\server.py` executa o servidor em sockets que valida cpf.

### Execução Clients:
`python .\grpc\client.py` executa o cliente irá se conectar ao servidor grpc.

`python .\valida_cpf\client.py` executa o cliente em sockets que quer validar um cpf.
