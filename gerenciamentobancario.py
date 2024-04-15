from datetime import datetime

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def abrir_conta_corrente(self, numero_conta, saldo_inicial=0):
        conta_corrente = ContaCorrente(numero_conta, saldo_inicial)
        self.contas.append(conta_corrente)
        return conta_corrente

    def abrir_conta_poupanca(self, numero_conta, saldo_inicial=0, taxa_juros=0.03):
        conta_poupanca = ContaPoupanca(numero_conta, saldo_inicial, taxa_juros)
        self.contas.append(conta_poupanca)
        return conta_poupanca

class Conta:
    def __init__(self, numero_conta, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.registrar_transacao(valor, "Depósito")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.registrar_transacao(valor, "Saque")
        else:
            print("Saldo insuficiente.")

    def registrar_transacao(self, valor, tipo):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.transacoes.append((data_hora, tipo, valor))

    def extrato(self):
        print(f"Extrato da Conta {self.numero_conta}:")
        for transacao in self.transacoes:
            print(f"{transacao[0]} - {transacao[1]}: R${transacao[2]}")
        print(f"Saldo Atual: R${self.saldo:.2f}")

class ContaCorrente(Conta):
    def __init__(self, numero_conta, saldo_inicial=0):
        super().__init__(numero_conta, saldo_inicial)
        self.tipo = "Corrente"

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, saldo_inicial=0, taxa_juros=0.03):
        super().__init__(numero_conta, saldo_inicial)
        self.tipo = "Poupança"
        self.taxa_juros = taxa_juros

    def calcular_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        self.registrar_transacao(juros, "Juros")

if __name__ == "__main__":
  
    cliente1 = Cliente("João", "123.456.789-00")
    cliente2 = Cliente("Maria", "987.654.321-00")

    conta1 = cliente1.abrir_conta_corrente("CC1", 1000)
    conta2 = cliente1.abrir_conta_poupanca("CP1", 500)
    conta3 = cliente2.abrir_conta_corrente("CC2", 2000)

    conta1.depositar(500)
    conta1.sacar(200)
    conta1.extrato()

    conta2.depositar(100)
    conta2.calcular_juros()
    conta2.extrato()

    conta3.sacar(500)
    conta3.extrato()
