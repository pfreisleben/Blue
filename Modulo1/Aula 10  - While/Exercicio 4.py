""" Codifique um jogo da FORCA. A pessoa digita uma palavra e tem que acertar a 
palavra digitada. """
palavra = input("Digite a palavra do jogo")
palavraOculta = ""
tentativas = []
for letra in palavra:
    palavraOculta += "_ "

while "_" in palavraOculta:
print(f' Palavra a ser acertada: {palavraOculta} ')
palpite = input("Digite uma letra para tentar completar a palavra: ")
while palpite in tentativas:
