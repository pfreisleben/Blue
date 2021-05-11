# Declaração de variável global e dentro do escopo da função
global a
a = 10


def soma(x, y):
    var = x + y
    print(a)
    return var


###########################################################################
# Função com valor padrão


def aumento_salarial(salario=5000, percentual=10):
    return salario*percentual/100 + salario


def reducao_salarial(salario=5000, percentual=10):
    return salario-salario*percentual/100
