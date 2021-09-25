class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura
    def alturaGet(self):
        return self._altura
    def idadeGet(self):
        return self._idade
    def envelhecer(self, anos_bem_vividos):
        i = 0
        while i < anos_bem_vividos:
            self._altura += 0.5
            self._idade += 1
            i += 1
    def engordar(self, peso_adquirido):
        self._peso += peso_adquirido
    def emagrecer(self, peso_perdido):
        self._peso -= peso_perdido


misterM = Pessoa("Gabriel Fallen Tolêdo", 14, 45.3, 1.5)
print(misterM.idadeGet())
print(misterM.alturaGet())
misterM.envelhecer(7)
print(misterM.idadeGet())
print(misterM.alturaGet())

