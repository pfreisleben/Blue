"""
Desenvolva um código que pergunte um número n para o usuário e exiba todos seus 
divisores. Caso seja um número primo, o programa ainda deve informar que se 
trata de um número primo! """

numero = int(input("Digite um número: "))
divisores = []

if numero % 2 != 0:
    print("O número é primo!")
for num in list(range(1, numero + 1)):
    if numero % num == 0:
        divisores.append(num)

print(f'Os divisores do item é/são: {divisores}')
