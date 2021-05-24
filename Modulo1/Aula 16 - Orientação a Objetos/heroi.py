class Herói():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def engordar(self, peso):
        self.peso += peso


a = Herói('Capitão América', 30, 85)
print(vars(a))
a.engordar(10)
print(vars(a))


class Pessoa():
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def emagrecer(self, peso):
        self.peso -= peso


a = Pessoa('Steve Rogers', 1.80, 90)
print(vars(a))
a.emagrecer(10)
print(vars(a))
a.peso = 100
print(vars(a))
