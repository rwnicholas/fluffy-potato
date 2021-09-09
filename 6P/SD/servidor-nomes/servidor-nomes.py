#!/usr/bin/python3

import pickle, sqlite3, socket

HOST = '127.0.0.1'
PORT = 39400

# banco de dados
database = sqlite3.connect("name_addr.db", check_same_thread=False)
cursor = database.cursor()
# criando a tabela de nomes e atributos
cursor.execute("CREATE TABLE IF NOT EXISTS nomes_atributos ("
    +"id INTEGER PRIMARY KEY AUTOINCREMENT,"
    +"nome TEXT NOT NULL,"
    +"addr TEXT NOT NULL,"
    +"atr_1 TEXT NOT NULL,"
    +"atr_2 TEXT NOT NULL,"
    +"atr_3 TEXT NOT NULL,"
    +"UNIQUE ( nome, atr_1, atr_2, atr_3 )"
    +")")

def lookup(atributos, nome = None):
    sql_select_query = "SELECT * FROM nomes_atributos WHERE"
    parameters = []
    try:
        if (nome == atributos == None):
            raise sqlite3.Error
        
        if nome != None:
            sql_select_query+= " nome = ?"
            parameters.append(nome)
            need_and = True
        
        elif atributos != None:
            sql_select_query+= " atr_1 = ?"
            parameters.append(atributos[0])

            sql_select_query+= " OR atr_2 = ?"
            parameters.append(atributos[0])

            sql_select_query+= " OR atr_3 = ?"
            parameters.append(atributos[0])

            for atrI in range(1, len(atributos)):
                sql_select_query+= " OR atr_1 = ?"
                parameters.append(atributos[atrI])

                sql_select_query+= " OR atr_2 = ?"
                parameters.append(atributos[atrI])

                sql_select_query+= " OR atr_3 = ?"
                parameters.append(atributos[atrI])
        
        cursor.execute(sql_select_query, parameters)
        r = [dict((cursor.description[i][0], value) \
                for i, value in enumerate(row)) for row in cursor.fetchall()]
        
        ## Mudando o formato de addr de texto para tupla HOST,PORT
        for x in r:
            addr = x['addr']
            tmp = addr[1:-1]
            tmp = tuple(tmp.split(', '))
            x['addr'] = (tmp[0], int(tmp[1]))
        
        return pickle.dumps(r)
    except sqlite3.Error as e:
        print(e.args)
        return pickle.dumps({'status': 'error'})

def bind(nome, addr, atr_1, atr_2, atr_3):
    try:
        cursor.execute("INSERT OR REPLACE INTO nomes_atributos (nome, addr, atr_1, atr_2, atr_3)"
            +" VALUES (?,?,?,?,?)",
            (nome,addr,atr_1,atr_2,atr_3))
        database.commit()

        return pickle.dumps({'status': 'ok'})
    except sqlite3.Error as e:
        print(e.args)
        return pickle.dumps({'status': 'error'})
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.bind((HOST, PORT))
    soc.listen()
    while True:
        conn, addr = soc.accept()
        print('Conectado por', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conteudo = pickle.loads(data)
            try:
                if conteudo['type'] == 'bind':
                    conn.sendall(bind(conteudo['nome'],conteudo['addr'],conteudo['atr_1'],conteudo['atr_2'],conteudo['atr_3']))
                elif conteudo['type'] == 'lookup':
                    ctd = dict(conteudo).copy()
                    del ctd['type']
                    conn.sendall(lookup(**ctd))
                else:
                    raise TypeError
            except:
                conn.sendall(pickle.dumps({'status': 'error'}))
