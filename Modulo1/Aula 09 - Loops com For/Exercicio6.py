""" Faça um script que peça ao usuário o número de matérias da escola, ou seja, 
um inteiro positivo. Em seguida, ele vai digitando o valor de cada nota, de cada
 matéria e isso será armazenado numa lista. Ao final, seu script deverá fornecer 
 a média geral do aluno. """
materias = int(input("Digite a quantidade de matérias: "))
notas = []
for materia in range(1, materias+1):
    nota = int(input(f'Digite a nota da matéria {materia}: '))
    notas.append(nota)
media = sum(notas)/materias
print(f'A média geral do aluno é: {media}')
