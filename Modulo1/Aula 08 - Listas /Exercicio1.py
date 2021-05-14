"""
    1. Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima 
    as seguintes informações:
        a. tamanho da lista.
        b. maior valor da lista.
        c. menor valor da lista.
        d. soma de todos os elementos da lista.
        e. lista em ordem crescente.
        f. lista em ordem decrescente.
"""
lista = [5, 7, 2, 9, 4, 1, 3]
print(f'Tamanho: {len(lista)}')
print(f'Maior: {max(lista)}')
print(f'Menor: {min(lista)}')
print(f'Soma: {sum(lista)}')
lista.sort()
print(f'Ordem crescente: {lista}')
lista.sort(reverse=True)
print(f'Ordem decrescente: {lista}')
