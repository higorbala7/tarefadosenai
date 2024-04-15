class Funcionario:
    def __init__(self, nome, id, salario):
        self.nome = nome
        self.id = id
        self.salario = salario

    def aumentar_salario(self, percentual):
        self.salario *= (1 + percentual / 100)


class Gerente(Funcionario):
    def __init__(self, nome, id, salario, departamento):
        super().__init__(nome, id, salario)
        self.departamento = departamento

    def promover_funcionario(self, funcionario):
        funcionario.aumentar_salario(10)


class FuncionarioRegular(Funcionario):
    pass


def calcular_folha_pagamento(lista_funcionarios):
    total_folha_pagamento = 0
    for funcionario in lista_funcionarios:
        total_folha_pagamento += funcionario.salario
    return total_folha_pagamento


funcionario1 = FuncionarioRegular("João", 1, 2000)
funcionario2 = FuncionarioRegular("Maria", 2, 2200)
gerente1 = Gerente("Carlos", 3, 3000, "TI")
gerente2 = Gerente("Ana", 4, 3200, "RH")


lista_funcionarios = [funcionario1, funcionario2, gerente1, gerente2]
total_folha_pagamento = calcular_folha_pagamento(lista_funcionarios)
print("Total da folha de pagamento:", total_folha_pagamento)
