import sqlite3, os

nomeBD = input("Nome do BD: ")

try:
    conector = sqlite3.connect(nomeBD)
    cursor = conector.cursor()
    id = '1'
    while id != '0':
        id = input("Digite o índice [0 - Sair]: ")
        if id != '0':
            nome = input("Nome: ")
            cursor.execute("UPDATE AGENDA SET NOME = ? WHERE ID = ?", (nome, id))
            conector.commit()
            print("Tabela atualizada :)")
    cursor.close()
    conector.close()

except sqlite3.Error as erro:
    print("Erro: ",erro)