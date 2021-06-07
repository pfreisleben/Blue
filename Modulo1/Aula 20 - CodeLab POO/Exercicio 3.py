class elevador():
    def __init__(self, andares, capacidade):
        self.andar = 0
        self.andares = andares
        self.capacidade = capacidade
        self.pessoas = 0

    def __str__(self):
        return f'O elevador está no andar {self.andar}, e possui {self.pessoas} pessoas dentro.'

    def entrar(self):
        if self.pessoas < self.capacidade:
            print(f'A(s) pessoa(s) entraram com sucesso no elevador.')
            self.pessoas += 1
        else:
            print(f'O elevador já está cheio, não cabe ninguém!')

    def sair(self):
        if self.pessoas == 0:
            print(f'Não tem ninguém no elevador! ')
        else:
            print(f'Uma pessoa saiu do elevador.')
            self.pessoas -= 1

    def subir(self):
        if self.andar == self.andares:
            print(f'O elevador está no último andar!')
        else:
            print(f'Subindo um andar!')
            self.andar += 1

    def descer(self):
        if self.andar == 0:
            print(f'O elevador já está no térreo!')
        else:
            print(f'Descendo um andar!')
            self.andar -= 1


elevador1 = elevador(10, 10)

elevador1.subir()
print(elevador1)
elevador1.descer()
print(elevador1)
elevador1.entrar()
print(elevador1)
elevador1.subir()
elevador1.subir()
elevador1.sair()
elevador1.sair()
print(elevador1)
