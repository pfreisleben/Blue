""" Desenvolver um programa para verificar a nota do aluno em uma prova com 10 
questões, o programa deve perguntar ao aluno a resposta de cada questão e ao 
final comparar com o gabarito da prova assim calcular o total de acertos e a 
nota (atribuir 1 ponto por resposta certa).  Após cada aluno utilizar o sistema 
deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:
    • Maior e Menor Acerto;
    • Total de Alunos que utilizaram o sistema;
    • A Média das Notas da Turma.
# Gabarito da Prova:
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
Após concluir isto você poderia incrementar o programa permitindo que o 
professor digite o gabarito da prova # antes dos alunos usarem o programa. """
alunos = []
nota = []
gabarito = ["a", "b", "c", "d", "e", "e", "d", "c", "b", "a"]
continua = True

while continua:
    acertos = 0
    nome = input("Aluno, digite o seu nome: ")
    for questao in range(len(gabarito)):
        resposta = input(
            f'Digite a resposta para a pergunta {questao + 1}: ').lower()
        if resposta == gabarito[questao]:
            acertos += 1
    alunos.append(nome)
    nota.append(acertos)
    deveContinuar = input("Outro aluno vai utilizar o sistema? S/N ").lower()
    if deveContinuar == 'n':
        continua = False
print(f'Maior acerto: {max(nota)}')
print(f'Menor acerto: {min(nota)}')
print(f'Quantidade de alunos que utilizaram: {len(alunos)}')
print(f'A média da sala é: {sum(nota) / len(nota)} ')
