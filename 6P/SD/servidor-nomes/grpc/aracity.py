#!/usr/bin/python3
import sqlite3
from sqlite3.dbapi2 import connect

def entrega_produto(produto, data_entrega, status, db = sqlite3.connect("aracity.db", check_same_thread=False)):
    try:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS situacao_produtos (produto TEXT, data_entrega DATE, status TEXT CHECK( status IN ('FALHA','SUCESSO') ))")

        cursor.execute("INSERT INTO `situacao_produtos` (`produto`,`data_entrega`,`status`) VALUES (?,?,?)", (produto, data_entrega, status))

        db.commit()
        
        return "Okay"
    except sqlite3.Error as e:
        print(e.args)
        return "Error"