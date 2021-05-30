import time


class bombaCombustivel:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def __str__(self):
        return f'Tipo de combustivel atual: {self.tipoCombustivel}, valor atual: {self.valorLitro}, quantidade atual: {self.quantidadeCombustivel:.2f}'

    def abastecerPorValor(self):
        valor = float(input("Digite o valor a ser abastecido: "))
        qtdLitros = valor / self.valorLitro
        self.quantidadeCombustivel -= qtdLitros
        self.abastecer(qtdLitros)
        print(f'Total a pagar: R${valor:.2f}')
        return qtdLitros

    def abastecerPorLitro(self):
        litro = float(
            input("Digite a quantidade em litros a ser abastecida: "))
        vlrAbastecimento = litro * self.valorLitro
        self.quantidadeCombustivel -= litro
        self.abastecer(litro)
        print(f'Total a pagar: R$ {vlrAbastecimento:.2f}')
        return vlrAbastecimento

    def alterarValor(self):
        novoValor = float(input("Informe o novo valor por litro: "))
        self.valorLitro = float(novoValor)

    def alterarCombustivel(self):
        novoCombustivel = input("Informe o novo combustivel: ")
        self.tipoCombustivel = novoCombustivel

    def alterarQuantidadeCombustivel(self):
        novaQuantidade = float(
            input("Digite a nova quantidade disponivel de combustivel: "))
        self.quantidadeCombustivel = novaQuantidade

    def abastecer(self, litros):
        litrosInteiro = int(litros)
        sobra = litros - litrosInteiro
        for i in range(1, int(litros)+1):
            print(f'Abastecendo.... {i} {"litro" if i == 1 else "litros"}.')
            time.sleep(0.5)
        if sobra > 0:
            print(f'Abastecendo... {sobra:.2f} litro.')

    def retornaValor(self):
        return self.valorLitro
