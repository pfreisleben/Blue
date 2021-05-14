"""
Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo
 texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de 
 ser enforcado."""

palavra = input("Informe a palavra: ").lower()
palavraOculta = ""
chances = 0
for letra in range(len(palavra)):
    palavraOculta = palavraOculta + "_"
for i in range(len(palavra)):
    if i >= 6:
        print("Você esgotou suas chances, cabô!")
        break
    else:
        print(f'Você ainda tem {6-i} chances! ')
        print("Palavra a ser advinhada: ")
        print(palavraOculta)
        palpite = input(
            "Digite uma letra e tente completar a palavra: ").lower()
        for index in range(len(palavra)):
            if palavra[index] == palpite:
                palavraOculta = list(palavraOculta)
                palavraOculta[index] = palpite
                string = ''.join(palavraOculta)
                palavraOculta = string
