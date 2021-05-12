""" Exercício Treino 1 - Escreva uma função que recebe dois parâmetros (números)
 e imprime o menor dos dois. Se eles forem iguais, imprima que são valores idênt
 icos. """


from datetime import date


def print_menor_igual(n1, n2):
    if n1 == n2:
        print("Os valores são idênticos.")
    elif n1 < n2:
        print(f'O número {n1} é o menor.')
    else:
        print(f'O número {n2} é o menor.')


print_menor_igual(5, 4)
