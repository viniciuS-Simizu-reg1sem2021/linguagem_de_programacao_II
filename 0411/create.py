import sqlite3
import os

nomeDB = input("Nome do BD: ")
conector = sqlite3.connect(nomeDB)
cursor = conector.cursor()
cursor.execute("CREATE TABLE AGENDA (ID INTEGER, NOME TEXT, FONE TEXT)")
id = 1
nome = "Pessoa"
while nome != '':
    print("ID:", id)
    nome = input("Nome: ")
    if nome != '':
        fone = input("Fone: ")
        cursor.execute("INSERT INTO AGENDA (ID, NOME, FONE) VALUES (?, ?, ?)", (id, nome, fone))
        conector.commit()
        id += 1
cursor.close()
conector.close()
print("BD criado com êxito:", nomeDB)
