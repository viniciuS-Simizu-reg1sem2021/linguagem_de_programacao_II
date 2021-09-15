salario_atual = float(input("Digite o seu sálario para reajuste: "))
if salario_atual > 0:
    taxa_reajuste = 0
    if salario_atual > 0 and salario_atual < 500:
        taxa_reajuste = .15
    elif salario_atual >= 500 and salario_atual <= 1000:
        taxa_reajuste = .10
    else:
        taxa_reajuste = .5
    aumento_salarial = salario_atual * taxa_reajuste
    print(f"Parabéns, agora o seu salário é de {salario_atual + aumento_salarial}")
else:
    print(f"Digite um valor positivo >:(")