import sqlite3, os

nomeBD = input("Nome do BD: ")
try:
    conector = sqlite3.connect(nomeBD)
    id = '1'
    cursor = conector.cursor()
    while id != '0':
        id = input("Digite o índice [0 - Sair]: ")
        if id != '0':
            cursor.execute("SELECT * FROM AGENDA WHERE ID=?", id)
            rs = cursor.fetchall()
            achei = False
            for contato in rs:
                print("ID: %d\nNome: %s\nFone: %s" % contato)
                achei = True
            if not achei:
                print("Erro: Contato não encontrado")
    cursor.close()
    conector.close()

except sqlite3.Error as erro:
    print("Erro: BD não encontrado")
    print("Erro: ", erro)
    os.remove(nomeBD)
