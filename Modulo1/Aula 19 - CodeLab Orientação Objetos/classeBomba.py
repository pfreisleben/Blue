import time


class bombaCombustivel:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        qtdLitros = valor / self.valorLitro
        self.quantidadeCombustivel -= qtdLitros
        return qtdLitros

    def abastecerPorLitro(self, litro):
        vlrAbastecimento = litro * self.valorLitro
        self.quantidadeCombustivel -= litro
        return vlrAbastecimento

    def alterarValor(self, novoValor):
        self.valorLitro = float(novoValor)

    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.quantidadeCombustivel = novaQuantidade

    def abastecer(self, litros):
        qtdAbastecida = 0
        for i in range(litros):
            print(f'Abastecendo.... {qtdAbastecida} litros.')
            qtdAbastecida += 1
            time.sleep(0.5)
