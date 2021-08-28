vetores = []
pares = []
impares = []

while len(vetores) < 20:
    valor = int(input(f"Insira o {len(vetores) + 1}° Número: "))
    vetores.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f"{sum(vetores)}\n{pares}\n{impares}")
