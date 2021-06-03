class ingresso ():
    def __init__(self, valor):
        self.valorReais = valor

    def imprimirValor(self):
        return self.valorReais


class ingressoVip(ingresso):
    def __init__(self, valor, valorExtra):
        self.valorExtra = valorExtra
        super().__init__(valor)

    def retornaValor(self):
        return self.valorReais + self.valorExtra


ingresso = ingresso(10)

ingressoVip = ingressoVip(10, 5)


print(
    f'A diferença entre os ingressos é: {ingressoVip.retornaValor() - ingresso.imprimirValor()}')
