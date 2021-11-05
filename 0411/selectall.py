import sqlite3
import os

nomeDB = input("Nome do BD: ")
try:
    conector = sqlite3.connect(nomeDB)
    cursor = conector.cursor()
    numRegistros = 0
    cursor.execute("SELECT * FROM AGENDA")
    result = cursor.fetchall()
    for contato in result:
        print("ID: %d\nNome: %s\nFone: %s" % contato)
        numRegistros += 1
    print(numRegistros, "registro(s)")
    cursor.close()
    conector.close()
except sqlite3.Error as erro:
    print("Erro? BD não encontrado ")
    print("Erro: ",erro)
    os.remove(nomeDB)
