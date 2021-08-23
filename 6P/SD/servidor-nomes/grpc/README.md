# Mini_Projeto 01
Para executar o sistema, lembrar de ter instalado tanto o `grpcio` quanto o `grpcio-tools`:
`pip install grpcio grpcio-tools`

### Execução:
O arquivo *server.py* é responsável por iniciar o servidor e executar a tarefa de salvar a entrega no banco de dados. Já o arquivo *client.py* é responsável por coletar os dados da entrega *(produto, data de entrega, e status da entrega)* e enviar ao servidor grpc, usando **protocolbuffer**.


`python3 .\server.py` executa o servidor.

`python3 .\client.py` executa o cliente.