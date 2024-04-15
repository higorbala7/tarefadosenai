class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print("O carro está ligado.")

    def desligar(self):
        self.ligado = False
        print("O carro está desligado.")

    def informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        if self.ligado:
            print("Status: Ligado")
        else:
            print("Status: Desligado")

carro1 = Carro("Toyota", "Corolla", 2020, "Prata")
carro2 = Carro("Honda", "Civic", 2018, "Preto")

carro1.informacoes()
print()
carro1.ligar()
carro1.informacoes()
print()
carro1.desligar()
carro1.informacoes()
print()
carro2.informacoes()
