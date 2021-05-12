
""" Exercício Treino 2 - Escreva uma função que recebe dois números (a e b) como
 parâmetro e retorna True caso a soma dos dois seja maior que um terceiro 
 parâmetro, chamado limite. """


def soma_limite(n1, n2, lim):
    soma = n1 + n2
    return soma > lim


print(soma_limite(1, 4, 6))
