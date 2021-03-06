""" (DESAFIO) Desenvolva um código em Python que gere um número aleatório de 1 
a 100 e dê ao usuário 10 chances para acertá-lo. A cada tentativa, deve ser 
impressa a quantidade de tentativas restantes e se o número aleatório é maior ou
 menor do que o número inserido na tentativa atual. Se o usuário não acertar em 
 10 tentativas, informe qual o número aleatório. [Dica: use a função randint 
 para gerar o número aleatório] """

import random

aleatorio = random.randint(1, 100)
chances = 0
while chances <= 10:
    print(f'Quantidade de tentativas restantes: {10-chances}')
    tentativa = int(input("Informe o número: "))
    if aleatorio > tentativa:
        print("O número aleatório é maior que a alternativa.")
    elif aleatorio < tentativa:
        print("O número aleatório é menor que a alternativa")
    else:
        print("Você acertou o número!")
        break
    chances += 1
