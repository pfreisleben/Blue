""" Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
quantidade de gols feito em cada partida. No final tudo isso será guardado em um
dicionário, incluindo o total de gols feitos durante o campeonato. """
aproveitamento = {}


def qtdGols(partidas):
    qtdTotal = 0
    for i in range(partidas):
        qtdTotal += int(
            input(f'Informe a quantidade de gols feitos na partida {i+1}: '))
    return qtdTotal


nome = input("Informe o nome do jogador: ")
qtdPartidas = int(
    input("Informe a quantidade de partidas jogadas pelo jogador: "))
aproveitamento.update({nome: qtdGols(qtdPartidas)})

print(aproveitamento)
