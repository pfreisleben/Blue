""" Crie um laço while que vai pedir para o usuário dois números e faça a soma 
dos dois. Enquanto a soma não for 50, ele deve continuar repetindo. """
soma = 0
while soma != 50:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    soma = n1 + n2
