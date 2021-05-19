""" DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
lista. No final, mostre:
A) Quantas pessoas estão cadastradas.
B) A média da idade.
C) Uma lista com as mulheres.
D) Uma lista com as idades que estão acima da média.
OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
perguntar ao usuário se deseja continuar a resposta seja somente sim ou não. """
from numpy import mean
pessoas = []
continua = True
while continua:
    print(f'Vamos iniciar um novo cadastro! ')
    pessoa = {}
    nome = input("Informe o seu nome: ").lower()
    sexo = input("Informe o seu sexo(M/F): ").lower()
    while sexo not in ("m", "f"):
        print(f'Sexo informado é inválido! Digite corretamente!')
        sexo = input("Informe o seu sexo(M/F): ")
    idade = int(input("Digite a sua idade: "))
    pessoas.append({"Nome": nome, "Sexo": sexo, "Idade": idade})
    deveContinuar = input("Uma nova pessoa irá se cadastrar? S/N").lower()
    while deveContinuar not in ("s", "n"):
        print(f'Opção digitada é incorreta, por favor selecione corretamente')
        deveContinuar = input("Uma nova pessoa irá se cadastrar? S/N").lower()
    if deveContinuar == "n":
        continua = False
print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
idades = []
for i in pessoas:
    idades.append(i["Idade"])
print(f'A média da idade das pessoas é: {mean(idades)}')
mulheres = []
for i in pessoas:
    if i.get("Sexo") == 'f':
        mulheres.append(i.get("Nome"))
print(f'As mulheres cadastradas são: {", ".join(mulheres)}')
idadeAcimaMedia = []
for i in pessoas:
    if i.get("Idade") > mean(idades):
        idadeAcimaMedia.append(str(i.get("Idade")))
print(f'As idades acima da média são: {",".join(idadeAcimaMedia)}')
