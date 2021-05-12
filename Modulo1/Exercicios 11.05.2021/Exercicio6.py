""" Exercício 6 - Um professor, muito legal, fez 3 provas durante um semestre, 
mas só vai levar em conta as duas notas mais altas para calcular a média. Faça
uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas
3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua 
nota mais baixa. """


def calculaNota(nota1, nota2, nota3):
    maior = nota1
    medio = nota1
    menor = nota1
    # Acha maior nota
    if nota2 > maior:
        maior = nota2
    elif nota3 > maior:
        maior = nota3
    # Acha segunda maior nota
    if maior >= nota2 > nota3:
        medio = nota2
    elif maior >= nota3 > nota2:
        medio = nota3
    elif maior >= nota1 > nota2:
        medio = nota1
    # Acha menor nota
    if nota2 < menor:
        menor = nota2
    if nota3 < menor:
        menor = nota3
    media_tres_notas = (nota1 + nota2 + nota3)/3
    media_notas_alta = (maior+medio) / 2
    print(f'Média com as três notas: {media_tres_notas}')
    print(f'Médias com duas melhores notas: {media_notas_alta}')
    print(f'Sua nota mais alta: {maior}')
    print(f'Sua nota mais baixa: {menor}')


calculaNota(10, 8, 9)
