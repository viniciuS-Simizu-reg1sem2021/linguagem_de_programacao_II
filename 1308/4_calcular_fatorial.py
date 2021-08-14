numero = abs(int(input("Digite um número a ser fatorado: ")))
fatorial = 1
for i in range(numero, 0, -1):
    fatorial *= i

print(fatorial)
