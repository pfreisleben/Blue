""" Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo sa estrutura na tela. A média para
aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
reprovado """

qtdAlunos = int(input("Digite a quantidade de alunos: "))
mediaAlunos = {
    "nome": [],
    "media": [],
    "situacao": []
}

for i in range(qtdAlunos):
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média do aluno: "))
    situacao = ""
    if media >= 7:
        situacao = "Aprovado"
    elif 5 > media <= 6.9:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    mediaAlunos["nome"].append(nome)
    mediaAlunos["media"].append(media)
    mediaAlunos["situacao"].append(situacao)

print(mediaAlunos)
