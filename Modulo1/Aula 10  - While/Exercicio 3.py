"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
Os códigos utilizados são:
    • 1 , 2, 3  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    • 5 - Voto Nulo
    • 6 - Voto em Branco
Faça um programa que calcule e mostre:
    • O total de votos para cada candidato;
    • O total de votos nulos;
    • O total de votos em branco;
    • A percentagem de votos nulos sobre o total de votos;
    • A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero. """

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
