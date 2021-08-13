numero = abs(int(input("Digite um número a ser fatorado: ")))
acumulador = 1
for i in range(numero, 0, -1):
    acumulador *= i

print(acumulador)
