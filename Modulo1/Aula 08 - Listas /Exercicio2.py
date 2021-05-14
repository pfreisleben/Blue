palavra = input("Informe a palavra: ").lower()
palavraOculta = ""
chances = 0
for letra in range(len(palavra)):
    palavraOculta = palavraOculta + "_"
for i in range(len(palavra)+6):
    if i == 6:
        print("Você não conseguiu completar a palvra.")
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
