""" Crie um programa em que 4 jogadores, joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário. No final coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado. Dicas: procure
sobre a função randint(), sleep() e itemgetter da bliblioteca operator. """
import time
import random
import operator
resultados = []
for i in range(1, 5):
    resultadoDado = random.randint(1, 6)
    print(f'Jogador {i} jogou o dado..')
    time.sleep(random.uniform(0.0, 1.0))
    print(f'O resultado é...')
    time.sleep(random.uniform(0.0, 1.0))
    print(f'É...')
    time.sleep(random.uniform(0.0, 1.0))
    print(f'O jogador {i} tirou {resultadoDado} no dado.')
    resultados.append((i, resultadoDado))
    time.sleep(2)
resultadoRanking = dict(sorted(resultados, key=operator.itemgetter(1)))
print(resultadoRanking)
