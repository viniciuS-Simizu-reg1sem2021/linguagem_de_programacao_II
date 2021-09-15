import math

def equacao (a:float, b:float, c:float):

	delta = b ** 2 - (4 * a * c)

	def calcula_raiz(delta):
		return (-b + delta) / (2 * a)



	raiz1 = calcula_raiz(math.sqrt(delta))
	raiz2 = calcula_raiz(-math.sqrt(delta))

	vertice = [-b / (2 * a), -delta / (4 * a)]

	print(f"\n1°raiz = ({raiz1}) e a 2°raiz = ({raiz2})\nDelta = ({delta})")

	if delta > 0:
		print("Raiz1 é diferente da Raiz2")
	elif delta < 0:
		print("A reta não cruza o eixo X")
	else:
		print("Raiz1 é igual a Raiz2")

	print()

	if a > 0:
		print(f"Ponto de Mínimo = {vertice}\nConcavidade virada para cima (U)")
	elif a < 0:
		print(f"Ponto de Máximo = {vertice}\nConcavidade virada para baixo (n)")



equacao(3, -8, 0)