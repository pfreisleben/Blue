class contaBancaria():
    def __init__(self, numero, agencia, tipo, saldo):
        self.numero = numero
        self.agencia = agencia
        self.codigo_tipo = tipo
        self.agenciasaldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise TypeError(
                "Valor inserido para saque é maior que o saldo atual da conta!")
        else:
            self.saldo -= valor

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito efetuado com sucesso!')
        else:
            print(f'Não é possivel depositar valores negativos! ')


class contaImposto(contaBancaria):
    def __init__(self, numero, agencia, tipo, saldo, percentualImposto):
        self.percentualImposto = percentualImposto
        super().__init__(numero, agencia, tipo, saldo)

    def calcularImposto(self):
        porcentagem = self.percentualImposto/100
        self.saldo -= self.saldo * porcentagem
