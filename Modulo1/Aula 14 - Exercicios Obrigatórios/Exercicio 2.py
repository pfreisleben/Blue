# 02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba
# uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais
# a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.
frase = input("Digite a frase: ").lower()
vogais = 0
for letra in frase:
    if letra in "aeiou":
        vogais += 1
        frase = frase.replace(letra, ' ')
print(f'Quantidade de vogais: {vogais}')
print(frase)
