try:
    salario_total: float = float(input("Digite o valor do seu sálario bruto: "))
    despesas: float = float(input("Digite o valor gasto em despesas: "))
    if salario_total - despesas >= 0:
        print("Gastos dentro do orçamento")
    else:
        print(f"Orçamento estourado >:(")

except:
    print("Pane no sistema, alguém me desconfigurou!!! >:(")
