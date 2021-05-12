
from datetime import date
""" Exercício 4 - Crie um programa que tenha uma função chamada voto () que vai 
receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor 
literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas 
eleições. Para resolver esse exercício, pesquise sobre a função date da bibli
oteca Datetime. """


def voto(birthYear):
    currentYear = int(date.today().year)
    difference = currentYear - birthYear
    if difference >= 16 and difference < 18:
        print("OPCIONAL")
    elif difference >= 18 and difference <= 70:
        print("OBRIGATÓRIO")
    else:
        print("NEGADO")


voto(2000)
