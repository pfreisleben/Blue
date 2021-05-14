"""Escreva um programa onde o usuário digita uma frase e essa frase retorna sem 
nenhuma vogal."""
frase = input("Digite uma frase: ")

for letra in frase:
    letra2 = letra.lower()
    if letra2 in "aeiou":
        frase = frase.replace(letra, " ")
print(frase)
