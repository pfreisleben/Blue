"""Faça um programa que leia dez conjuntos de dois valores, o primeiro
representando o número do aluno e o segundo representando a sua altura em
centímetros.  Encontre o aluno mais alto e o mais baixo. Mostre o número do
aluno mais alto e o número do aluno mais baixo, junto com suas alturas. """

numero = []
altura = []
conjuntos = 0
maisAlto = 0
maisBaixo = 0
while conjuntos < 10:
    al = int(input("Digite a altura em centimetros: "))
    if conjuntos == 0:
        maisAlto = al
        maisBaixo = al
    altura.append(al)
    numero.append(len(numero) + 1)
    conjuntos += 1
    if al > maisAlto:
        maisAlto = al
    if al < maisBaixo:
        maisBaixo = al
indexAlto = altura.index(maisAlto)
indexBaixo = altura.index(maisBaixo)

print(
    f'O aluno mais alto é: Número: {numero[indexAlto]} Altura: {altura[indexAlto]}cm')
print(
    f'O aluno mais baixo é: Número: {numero[indexBaixo]} Altura: {altura[indexBaixo]}cm')
