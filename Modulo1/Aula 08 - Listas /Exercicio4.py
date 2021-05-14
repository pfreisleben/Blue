"""
Dada uma string com uma frase informada pelo usuário (incluindo espaços em 
branco), conte quantas vezes aparece uma vogal."""

frase = input("Informe uma frase: ")
vogais = 0
for letra in frase:
    if letra in "aeiou":
        vogais = vogais + 1
print(f'Vogais aparecem {vogais} vezes')
