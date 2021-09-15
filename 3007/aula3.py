'''
import os
os.system("cls") # Limpa o prompt
os.system("notepad") # Abre o bloco de notas


valor = abs(int(input("Qual a sua idade? ")))
if valor < 18:
    print("Você foi hackeado pelo pedro quebrador de códigos\nPERDEU HAHAHHAHAHAHHAH%c" % (chr(33)))
elif valor > 18:
    print("Seu estrato bancario foi depositado com êxito :D")
else:
    print("lol cara vai trabalhar ksksks")


x = int(input("Digite o 1 valor: "))
y = int(input("Digite o 2 valor: "))
opt = input("Digite o tipo de operação: ")
if opt == '+':
    print(x + y)
elif opt == '-':
    print(x - y)
'''