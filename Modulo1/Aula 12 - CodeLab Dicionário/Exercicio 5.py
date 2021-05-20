"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0,
o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente , além da idade, com quantos anos a pessoa vai se aposentar.
Considere que o trabalhador deve contribuir por 35 anos para se aposentar."""
from datetime import date
trabalhador = {}


def calcTrabalhador(nome, nascimento, ctps=0):
    idade = int(date.today().year) - nascimento
    if ctps != 0:
        anoContratacao = int(input("Informe o ano de contratação: "))
        salario = float(input(("Informe o valor do salário: ")))
        anoAposentadoria = (anoContratacao + 35) - nascimento
        trabalhador[nome] = {"Ano de nascimento": nascimento,
                             "Idade": idade,
                             "Salario": salario,
                             "Idade de aposentadoria": anoAposentadoria}
    else:
        trabalhador[nome] = {"Ano de nascimento": nascimento, "Idade": idade}


calcTrabalhador("Pedro", 1997, 1)
print(trabalhador)
