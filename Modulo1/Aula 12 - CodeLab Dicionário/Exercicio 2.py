""" Crie um dicionário em que suas chaves correspondem a números
inteiros entre [1, 10] e cada valor associado é o número ao quadrado.
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100} """

dicionario = {}
for i in range(1, 11):
    dicionario[i] = i**2
print(dicionario)
