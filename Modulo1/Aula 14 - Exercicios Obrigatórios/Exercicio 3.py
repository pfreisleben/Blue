# 03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha
#  para iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após
#  entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador
# vai “pensar” em um número inteiro entre 0 e 20. O jogador vai tentar adivinhar qual número
# foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo
# computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram
# necessários para vencer.
import random
import time
senhaReal = "pedro"
senhaDigitada = input("Digite a senha para continuar! ")
while senhaDigitada != senhaReal:
    print(f'Senha incorreta, digite novamente!')
    senhaDigitada = input("Digite a senha para continuar!")

while senhaDigitada == senhaReal:
    print(f"Senha correta. Bem-vindo! ")
    print(f'O computador vai pensar em um número entre 0 e 20, e você deve acertá-lo.')
    time.sleep(1)
    print(f'O computador está pensando.... ')
    numeroComputador = random.randint(0, 20)
    time.sleep(2)
    print(f'Ok, o computador escolheu um número!')
    palpiteHumano = int(input("Digite o seu palpite: "))
    tentativas = 1
    while palpiteHumano != numeroComputador:
        print(f'Você errou, mas vamos te ajudar: ')
        if palpiteHumano < numeroComputador:
            print(f'O número que você digitou é menor do que o número a ser descoberto.')
        else:
            print(f'O número que você digitou é maior do que o número a ser descoberto.')
        palpiteHumano = int(input("Tente novamente, digite um novo número: "))
        tentativas += 1
    print(f'Parabéns, você acertou!')
    print(f'Quantidade de tentativas necessárias para vencer: {tentativas}')
    senhaDigitada = ""
