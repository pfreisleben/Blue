class pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def mostraDados(self):
        print(f'Nome: {self.nome} {self.sobrenome}, Idade: {self.idade}')


pedro = pessoa('Pedro', 'Freisleben', 23)

pedro.mostraDados()
