"""Faça um programa que calcule o salário de um colaborador na empresa XYZ.
 O salário é pago conforme a quantidade de horas trabalhadas. Quando um 
 funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas
  extras trabalhadas."""


def calcula_salario(horas, vlrHora):
    if horas <= 40:
        return horas * vlrHora
    elif horas > 40:
        vlrHrExtra = ((horas - 40)*vlrHora)*1.5
        hrNormal = horas - (horas - 40)
        return hrNormal * vlrHora + vlrHrExtra


print(calcula_salario(52, 10))
