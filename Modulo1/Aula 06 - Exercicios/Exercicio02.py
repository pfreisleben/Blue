"""
 Faça um programa, com uma função que necessite de um argumento. A função 
 retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu 
 argumento for negativo e ‘0’ se for 0.
 """


def retorna_valor(numero):
    if numero == 0:
        return 0
    elif numero > 0:
        return "P"
    else:
        return "N"
