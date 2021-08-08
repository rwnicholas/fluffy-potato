#!/usr/bin/python3
from flask import Flask, Response, request, jsonify

sucos = [
    {
        "id": 1,
        "nome": "laranja",
        "litros": 2.5
    },
    {
        "id": 2,
        "nome": "maçã",
        "litros": 3
    },
    {
        "id": 3,
        "nome": "manga",
        "litros": 1
    },
]

def get_next_id():
    return max(x['id'] for x in sucos)+1

app = Flask(__name__)

@app.route('/api/', methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH',  'OPTIONS'])
def main():
    if request.method == 'GET':
        return jsonify(sucos)

    elif request.method == 'POST':
        newSuco = {
            "id": get_next_id()
        }
        newSuco.update(request.json)
        sucos.append(newSuco)

        return jsonify(newSuco)

    elif request.method == 'PUT':
        ids = [x['id'] for x in sucos]
        if not request.json['id'] in ids:
            return Response(status=404)
        else:
            for i in sucos:
                if request.json['id'] == i['id']:
                    i.update(request.json)
            return Response(status=200)

    elif request.method == 'DELETE':
        ids = [x['id'] for x in sucos]
        returnedI = None
        if not int(request.args.get('id')) in ids:
            return Response(status=404)
        else:
            for i in sucos:
                if int(request.args.get('id')) == i['id']:
                    returnedI = i
                    sucos.remove(i)
            return jsonify(returnedI)
    elif request.method == 'OPTIONS':
        return Response(headers={'Allow':"GET, POST, PUT, DELETE, OPTIONS", 'Content-Type': 'application/json'})


app.run()