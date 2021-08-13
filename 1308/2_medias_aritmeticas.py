lista_de_numeros = []
numero_por_letra = {0: "A", 1: "B", 2: "C"}
i = abs(int(input("Digite o valor da letra 'i': ")))
print("Digite os números a serem calculados :)\n")
while len(lista_de_numeros) < 3:
    lista_de_numeros.append(float(input(f"Por favor, insira o valor da letra '{numero_por_letra[len(lista_de_numeros)]}': ")))
if i % 2 == 0:
    media = sum(lista_de_numeros) / 3
    print(f"A Média Aritmetica dos números inseridos é igual a {media}")
elif i > 10:
    media_ponderada = (lista_de_numeros[0] * 2 + lista_de_numeros[1] * 3 + lista_de_numeros[2] * 4) / 9
    print(f"A Média Ponderada dos números inseridos é igual a {media_ponderada}")


