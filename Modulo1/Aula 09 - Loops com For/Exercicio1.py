""" Crie um código em Python que pede qual tabuada o usuário quer ver, em 
seguida imprima essa tabuada. """


def tabuada():
    numero = int(input("Digite o número cuja tabuada deseja ver: "))
    for num in list(range(1, 11)):
        print(f'{numero}x{num} = {numero*num}')


tabuada()
