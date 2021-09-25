class Quadrado:
    def __init__(self, aresta: float):
        self._aresta = aresta
    def arestaSet(self, medida_aresta) -> None:
        self._aresta = medida_aresta
    def area(self) -> float:
        return self._aresta ** 2

quad = Quadrado(3.5)
print(f"{quad.area()}m2")
quad.arestaSet(9)
print(f"{quad.area()}m2")
