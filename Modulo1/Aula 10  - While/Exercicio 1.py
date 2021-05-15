"""
Exercício 1 - Escreva um programa que pede a senha ao usuário, e só sai do
looping quando digitarem corretamente a senha.  """

senha = "9856321"

digitada = input("Digite sua senha: ")
while digitada != senha:
    print("Senha incorreta, digite novamente!")
    digitada = input("Digite sua senha: ")
print(f'Você digitou a senha correta!')
