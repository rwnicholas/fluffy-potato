# Desenvolvimento de Web Services
Para executar o sistema, lembrar de ter instalado tanto o `flask` quanto o `requests`:
`pip install flask requests`

### Execução:
O arquivo *web_service.py* é responsável por iniciar o servidor e executar a tarefa de salvar a entrega no banco de dados. Já o arquivo *client.py* é responsável por coletar os dados da entrega *(produto, data de entrega, e status da entrega)* e enviar ao webservice, usando **JSON**.


`python3 .\web_service.py` executa o servidor.

`python3 .\client.py` executa o cliente.