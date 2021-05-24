# 06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:

# "Telefonou para a vítima?"

# "Esteve no local do crime?"

# "Mora perto da vítima?"

# "Devia para a vítima?"

# "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.

# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",

# Entre 3 e 4 como "Cúmplice" e 5 como "Assassino".

# Caso contrário, ele será classificado como "Inocente".

perguntas = ["Telefonou para vítima? S/N ",
             "Esteve no local do crime? S/N ", "Mora perto da vítima? S/N ",
             "Devia para a vítima? S/N ", "Já trabalhou com a vítima? S/N "]
respostas = []

for pergunta in perguntas:
    resposta = input(pergunta).lower()
    if resposta == 's' or resposta == 'n':
        respostas.append(resposta)
    else:
        respostas.clear()
        print("Resposta inválida!")
        break

respostaSim = respostas.count("s")

if len(respostas) == 0:
    print("Nenhuma resposta válida, encerrando.")
else:
    if respostaSim < 2:
        print("Você é inocente!")
    elif respostaSim == 2:
        print("Você é suspeito!")
    elif respostaSim >= 3 and respostaSim <= 4:
        print("Você é cúmplice!")
    elif respostaSim == 5:
        print("Você é o Assassino.")
