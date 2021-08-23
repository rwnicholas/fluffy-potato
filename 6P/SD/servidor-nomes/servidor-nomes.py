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
    +"atr_operacao TEXT NOT NULL,"
    +"atr_entrada TEXT NOT NULL,"
    +"atr_entrada_type TEXT CHECK( atr_entrada_type IN ('json','text', 'protocolbuffer') ) NOT NULL,"
    +"UNIQUE ( nome, atr_operacao, atr_entrada, atr_entrada_type )"
    +")")

def lookup(nome = None, atr_operacao = None, atr_entrada = None, atr_entrada_type = None):
    sql_select_query = "SELECT nome,addr FROM nomes_atributos WHERE"
    need_and = False
    parameters = []
    try:
        if (nome == atr_operacao == atr_entrada == atr_entrada_type == None):
            raise sqlite3.Error
        
        if nome != None:
            sql_select_query+= " nome = ?"
            parameters.append(nome)
            need_and = True
        
        if atr_operacao != None:
            if need_and:
                sql_select_query+= " AND atr_operacao = ?"
                parameters.append(atr_operacao)
            else:
                sql_select_query+= " atr_operacao = ?"
                parameters.append(atr_operacao)
                need_and = True

        if atr_entrada != None:
            if need_and:
                sql_select_query+= " AND atr_entrada = ?"
                parameters.append(atr_entrada)
            else:
                sql_select_query+= " atr_entrada = ?"
                parameters.append(atr_entrada)
                need_and = True

        if atr_entrada_type != None:
            if need_and:
                sql_select_query+= " AND atr_entrada_type = ?"
                parameters.append(atr_entrada_type)
            else:
                sql_select_query+= " atr_entrada_type = ?"
                parameters.append(atr_entrada_type)
                need_and = True
        
        print(sql_select_query)
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

def bind(nome, addr, atr_operacao, atr_entrada, atr_entrada_type):
    try:
        cursor.execute("INSERT OR REPLACE INTO nomes_atributos (nome, addr, atr_operacao, atr_entrada, atr_entrada_type)"
            +" VALUES (?,?,?,?,?)",
            (nome,addr,atr_operacao,atr_entrada,atr_entrada_type))
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
        print('Conecatado por', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conteudo = pickle.loads(data)
            try:
                if conteudo['type'] == 'bind':
                    conn.sendall(bind(conteudo['nome'],conteudo['addr'],conteudo['atr_operacao'],conteudo['atr_entrada'],conteudo['atr_entrada_type']))
                elif conteudo['type'] == 'lookup':
                    ctd = dict(conteudo).copy()
                    del ctd['type']
                    conn.sendall(lookup(**ctd))
                else:
                    raise TypeError
            except:
                conn.sendall(pickle.dumps({'status': 'error'}))
