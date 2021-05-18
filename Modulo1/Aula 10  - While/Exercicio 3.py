opcoes = [1, 2, 3, 5, 6]
nomes = ["Jose", "João", "Pedro", "Voto Nulo", "Voto em Branco"]
votos = [0, 0, 0, 0, 0]  # Armazena votos em lista, todos iniciados com 0.

while True:
    print("Escolha sua opção de voto, ou digite 0 para sair: ")
    for op in range(len(opcoes)):
        print(f'{opcoes[op]} - {nomes[op]}')
    voto = int(input("Digite o número do seu voto: "))
    if voto != 0 and voto in opcoes:
        indexVoto = opcoes.index(voto)
        votos[indexVoto] += 1
    else:
        print("Votação encerrada.")
        break
for op in range(len(opcoes)):
    print(f'{nomes[op]} - {votos[op]} votos')
print(f'Porcentagem de votos nulos sobre o total: {votos[3]/sum(votos)*100}%')
print(
    f'Porcentagem de votos em branco sobre o total: {votos[4]/sum(votos)*100}%')
