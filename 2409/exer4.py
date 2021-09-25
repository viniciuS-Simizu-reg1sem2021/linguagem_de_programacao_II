class Bola:
    def __init__(self, cor: str, circunferencia: float, material: str) -> object:
        self._cor = cor
        self._circunferencia = circunferencia
        self._material = material

    def corSet(self, nova_cor):
        self._cor = nova_cor

    def corGet(self):
        return self._cor


bola_onze = Bola("Verde", 0.7, "Madeira")
print(bola_onze.corGet())
bola_onze.corSet("Marrom")
print(bola_onze.corGet())
