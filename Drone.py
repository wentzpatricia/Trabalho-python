from Veiculo import Veiculo
from Pilha import Pilha

pilhaDrones = Pilha()

class Drone(Veiculo):
    def __init__(self, marca, modelo, qtdHelices):
        self.marca = marca
        self.modelo = modelo
        self._qtdHelices = qtdHelices    

    def adicionar(self):
        valor = (f"""
    A marca do Drone é: {self.marca}
    O modelo é: {self.modelo}
    Qtd de Hélices: {self._qtdHelices}
            """)
        pilhaDrones.adicionar(valor)

    def remover(self):
        pilhaDrones.remover()

    def imprimir(self):
        pilhaDrones.imprimir()