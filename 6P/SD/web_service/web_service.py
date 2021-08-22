#!/usr/bin/python3
from flask import Flask, Response, request
import sqlite3, json

app = Flask(__name__)

@app.route('/api/', methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH',  'OPTIONS'])
def main():
    db = sqlite3.connect("aracity.db", check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS situacao_produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, produto TEXT, data_entrega DATE, status TEXT CHECK( status IN ('FALHA','SUCESSO') ))")

    if request.method == 'GET':
        cursor.execute("SELECT * FROM `situacao_produtos`")
        data = cursor.fetchall()
        return json.dumps(data)

    elif request.method == 'POST':
        try:
            cursor.execute("INSERT INTO `situacao_produtos` (`produto`,`data_entrega`,`status`) VALUES (?,?,?) RETURNING id", (request.json['produto'], request.json['data_entrega'], request.json['status']))
            id = int(cursor.lastrowid)

            cursor.execute("SELECT * FROM `situacao_produtos` WHERE id = ?", (id,))
            data = cursor.fetchone()
            db.commit()

            return Response(json.dumps(data), status=200)
        except sqlite3.Error as e:
            print(e.args)
            return Response(status=400)

    elif request.method == 'PUT':
        try:
            cursor.execute("UPDATE `situacao_produtos` SET produto = ?, data_entrega = ?, status = ? WHERE id = ?", (request.json['produto'], request.json['data_entrega'], request.json['status'], request.json['id']))
            db.commit()

            return Response(status=200)
        except sqlite3.Error as e:
            print(e.args)
            return Response(status=404)

    elif request.method == 'DELETE':
        try:
            cursor.execute("DELETE FROM `situacao_produtos` WHERE id = ?", (request.args.get('id')))
            db.commit()

            return Response(status=200)
        except sqlite3.Error as e:
            print(e.args)
            return Response(status=404)

    elif request.method == 'OPTIONS':
        return Response(headers={'Allow':"GET, POST, PUT, DELETE, OPTIONS", 'Content-Type': 'application/json'})


app.run()