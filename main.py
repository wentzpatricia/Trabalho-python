#Trabalho desenvolvido por Patrícia Wentz de Moraes
from Carro import Carro
from Pilha import Pilha
from Drone import Drone

pilhaCarro = Pilha()

pilhaDrone  = Pilha()

def adicionarCarro():
    marca = input("\nQual a marca do seu carro? ")
    modelo = input("Qual o modelo do seu carro? ")
    qtdPortas = input("Qtd Porta do seu carro? ")
    carro = Carro(marca, modelo, qtdPortas)
    
    carro.adicionar()
    while True:
        escolha = input(f"""\n\n
        ---------------------------------------------------
                    Digite a opção desejada
        ---------------------------------------------------
        1. Continuar adicionando Carros a pilha de carros
        2. Remover carros da pilha
        3. Imprimir pilha de carros
        0. Sair
        ---------------------------------------------------
        Escolha: """)

        if escolha == '1':
            adicionarCarro()
        elif escolha == '2':
            carro.remover()

        elif escolha == '3':
            print("\n\n------ PILHA DE CARROS ------")
            carro.imprimir()

        elif escolha == '0':
            menu()


def adicionarDrone():
    marca = input("\nQual a marca do seu Drone? ")
    modelo = input("Qual o modelo do seu Drone? ")
    qtdHelices = input("Qtd de Hélices do seu Drone? ")
    drone = Drone(marca, modelo, qtdHelices)
    
    drone.adicionar()
    while True:
        escolha = input(f"""\n\n
        ---------------------------------------------------
                    Digite a opção desejada
        ---------------------------------------------------
        1. Continuar adicionando Drones a pilha de drones
        2. Remover drones da pilha
        3. Imprimir pilha de drones
        0. Sair
        ---------------------------------------------------
        Escolha: """)

        if escolha == '1':
            adicionarDrone()
        elif escolha == '2':
            drone.remover()

        elif escolha == '3':
            print("\n\n------ PILHA DE DRONES ------")
            drone.imprimir()

        elif escolha == '0':
            menu()


def menu():
    while True:
        escolha = input(f"""\n\n
        ------------------------------
           Digite a opção desejada
        ------------------------------
        1. Adicionar Carros
        2. Adicionar Drones
        0. Sair
        ------------------------------
        Escolha: """)
    
        if escolha == '1':
            adicionarCarro()
        elif escolha == '2':
            adicionarDrone()
        elif escolha == '0':
            break

menu()