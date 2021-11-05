import sqlite3
import os

nomeBD = input("Nome do BD: ")

try:
    conector = sqlite3.connect(nomeBD)
    cursor = conector.cursor()
    id = '1'
    while id != '0':
        id = input("Digite o índice [0 - Sair]: ")
        if id != '0':
            cursor.execute("DELETE FROM AGENDA WHERE ID = ?", (id))
            conector.commit()
            print("Okay, contato removido")
    cursor.close()
    conector.close()

except sqlite3.Error as erro:
    print("Erro: BD não encontrado")
    print("Erro: ",erro)
    os.remove(nomeBD)
