lista = []
while len(lista) < 5:
    lista.append(int(input(f"Digite o {len(lista) + 1}° Número a ser inserido: ")))
print()

for elemento in lista:
    print(f"_{elemento}_")
