# 01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números
# e mostre:

# A soma deles;

# A multiplicação entre eles;

# A divisão inteira deles;

# Mostre na tela qual é o maior;

# Verifique se o resultado da soma é par ou impar e mostre na tela;

# Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e
# mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.
n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))
print(f' Soma dos números: {n1 + n2}')
print(f' Multiplicação entre os números: {n1 * n2}')
print(f' Divisão inteira deles: {n1//n2}')
if n1 > n2:
    print(f'Maior número: {n1}')
else:
    print(f'Maior número: {n2}')
if (n1+n2) % 2 == 0:
    print(f'O resultado da soma é par! Resultado: {n1+n2}')
else:
    print(f'O resultado da soma é impar! Resultado: {n1+n2}')
if n1 * n2 > 40:
    print(f'A multiplicação é maior que 40! Resultado: {(n1*n2)/(n1//n2)}')
else:
    print(f'A multiplicação não foi maior que 40.')
