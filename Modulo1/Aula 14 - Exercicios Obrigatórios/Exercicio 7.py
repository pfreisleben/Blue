# 07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares
#  e ímpares em ordem crescente.

lista = [[], []]
continua = 0
while continua < 7:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
    continua += 1
lista[0].sort()
lista[1].sort()
print(f'Lista de valores pares: {lista[0]}')
print(f'Lista de valores ímpares: {lista[1]}')
