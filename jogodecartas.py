import random

class Carta:
    naipes = ['Espadas', 'Paus', 'Copas', 'Ouros']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

class Baralho:
    def __init__(self):
        self.cartas = [Carta(valor, naipe) for naipe in Carta.naipes for valor in Carta.valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir_cartas(self, num_cartas):
        return [self.cartas.pop() for _ in range(num_cartas)]

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receber_carta(self, carta):
        self.mao.append(carta)

    def mostrar_mao(self):
        print(f"Cartas do jogador {self.nome}:")
        for carta in self.mao:
            print(carta)

if __name__ == "__main__":

    baralho = Baralho()
    baralho.embaralhar()

    jogador1 = Jogador("Jogador 1")
    jogador2 = Jogador("Jogador 2")

    num_cartas_por_jogador = 5
    jogador1.receber_carta(baralho.distribuir_cartas(num_cartas_por_jogador))
    jogador2.receber_carta(baralho.distribuir_cartas(num_cartas_por_jogador))

    jogador1.mostrar_mao()
    print()
    jogador2.mostrar_mao()
