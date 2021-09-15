def soma_impar(x, y):
    lista = None
    if x % 2 == 0:
        lista = range(x+1, y+1, 2)
    else:
        lista = range(x, y+1, 2)
    print(sum(lista))

soma_impar(2, 20)
