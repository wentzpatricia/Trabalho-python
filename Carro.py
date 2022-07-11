from Veiculo import Veiculo
from Pilha import Pilha

pilhaCarros = Pilha()

class Carro(Veiculo):
    def __init__(self, marca, modelo, qtdPortas):
        self.marca = marca
        self.modelo = modelo
        self.__qtdPortas = qtdPortas     

    def adicionar(self):
        valor = (f"""
    A marca do carro é: {self.marca}
    O modelo é: {self.modelo}
    Qtd de portas: {self.__qtdPortas}
            """)
        pilhaCarros.adicionar(valor)

    def remover(self):
        pilhaCarros.remover()

    def imprimir(self):
        pilhaCarros.imprimir()