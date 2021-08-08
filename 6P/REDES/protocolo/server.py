#!/usr/bin/python3

import socket
import _thread
import json

HOST = '127.0.0.1'
PORT = 39400

database = [
    {
        "from": "nicholas",
        "to": "geralt",
        "message": "Como vão as aventuras?"
    },
    {
        "from": "triss",
        "to": "nicholas",
        "message": "Já tomou a vacina?"
    },
    {
        "from": "jaskier",
        "to": "nicholas",
        "message": "#ForaBolsonaro"
    },
]


'''
    Protocolo de mensagens entre usuários:
        1- Enviar mensagem para usuário (send_message)
        2- Ler mensagens (read_message)
    Formato: 
        content_format {
            "from": sender
            "to": reciever
            "message": message
        }

        protocol {
            send: True | False
            read: True | False
            content: content_format
        }
'''

def read(to_):
    users = [x['to'] for x in database]
    if to_ in users:
        mensagens = []
        for m in database:
            if to_ == m['to']:
                mensagens.append(m)
        return {"mensagens": mensagens}
    else:
        return {"error": 404, "reason": "Nenhuma mensagem para " + to_}

def send(from_, to_, message_):
    if (from_ != None and to_ != None and message_ != None) and (from_ != "" and to_ != "" and message_ != ""):
        newMessage = {
            "from": from_,
            "to": to_,
            "message": message_
        }
        database.append(newMessage)
        return {"message-sent": 'OK'}
    else:
        return {"error": 400, "reason": "Message body incomplete!"}
def process_request(data):
    try:
        output = {}
        if data['content'] != None:
            if data['send'] == True:
                content = data['content']
                output.update(send(content['from'], content['to'], content['message']))
            if data['read'] == True:
                output.update(read(data['content']['from']))

        return json.dumps(output).encode('utf-8')
    except:
        return b'{"error": 400, "reason": "Body incomplete!"}'

def new_client(conn, addr):
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(process_request(json.loads(data.decode('utf-8'))))
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.bind((HOST, PORT))
    soc.listen()
    while True:
        conn, addr = soc.accept()
        _thread.start_new_thread(new_client, (conn, addr))