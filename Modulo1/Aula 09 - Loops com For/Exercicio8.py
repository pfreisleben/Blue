"""     8. (DESAFIO) Escreva um programa que determine todos os números de 4 
algarismos que possam ser separados em dois números de dois algarismos que 
somados e elevando-se a soma ao quadrado obtenha-se o próprio número.

Exemplo: 3025 = 55 e 55**2 é igual á 3025"""
numeros = []

for num in range(1000, 10000):
    # Retorna o inteiro da divisão, não considerando a sobra. => 3025/100 = 30,25
    doisPrimeiros = num // 100
    doisSegundos = num % 100  # Retorna a sobra da divisão
    if (doisPrimeiros+doisSegundos) ** 2 == num:
        numeros.append(num)
print(numeros)
