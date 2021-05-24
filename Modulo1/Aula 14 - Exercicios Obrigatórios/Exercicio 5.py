# 05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário
#  e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas
#  da frase original.

def converteFrase(frase):
    for letra in frase:
        if letra in "aeiou":
            frase = frase.replace(letra, '')
    return frase


frase = input("Digite a frase: ")
novaFrase = converteFrase(frase)

print(f'A nova frase é: {novaFrase}')
print(
    f'Quantida de letras retiradas da frase original: {len(frase) - len(novaFrase)}')
