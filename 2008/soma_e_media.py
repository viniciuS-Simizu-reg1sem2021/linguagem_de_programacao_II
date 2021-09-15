entrada = 1
lista_de_numeros = []
lista_de_numeros.append(int(input("Digite o 1°Número a ser processado: ")))
while entrada != 0:
    lista_de_numeros.append(int(input(f"Digite o {len(lista_de_numeros) + 1}°Número a ser processado: ")))
    entrada = int(input("Precione '0' para encerrar o processo, caso contrario, digite 1\n"))
print("Soma = ",sum(lista_de_numeros), "\nMédia = ", sum(lista_de_numeros) / len(lista_de_numeros))

