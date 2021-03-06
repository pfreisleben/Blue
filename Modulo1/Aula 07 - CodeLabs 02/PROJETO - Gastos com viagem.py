""" PROJETO: Gastos com viagem -  Escrever uma aplicação utilizando funções que 
calcule os gastos com passagem, hospedagem, aluguel de carro e gastos extras de 
uma viagem para uma determinada cidade.

1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) 
chamado 'noites' e retorne o custo total do hotel, sendo que 1 noite custa R$ 140,00.

"""


def custo_hotel(noites):
    return 140 * noites


"""2 - Crie uma função chamada 'custo_aviao' que receba o nome da cidade e 
retorne o custo da passagem de avião, sendo que passagem para:

- São Paulo custa R$ 312,00;

- Porto Alegre custa R$ 447,00;

- Recife custa R$ 831,00;

- Manaus custa R$ 986,00.
"""


def custo_aviao(cidade):
    cidade = cidade.lower()
    if cidade == "são paulo":
        return 312.00
    elif cidade == "porto alegre":
        return 447.00
    elif cidade == "recife":
        return 831.00
    elif cidade == "manaus":
        return 986.00


""" 3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.

- Calcule o custo do aluguel do carro sendo que:

- A cada dia o carro custa R$ 40,00;

- Alugando 7 dias ou +: R$ 50,00 de desconto;

- Alugando 3 dias ou +: R$ 20,00 de desconto;

- Você pode receber apenas um desconto;

- Retorne o custo. """


def custo_carro(dias):
    aluguel = dias * 40
    if dias >= 7:
        aluguel = aluguel - 50
    elif dias >= 3:
        aluguel = aluguel - 20
    return aluguel


""" 4 - Agora com essas três funções criadas, declare uma função que receba a 
cidade e quantidade de dias e retorne o custo total da viagem.

- Reutilize as funções já criadas.

- Exiba o total da viagem chamando apenas a nova função declarada! """


def custo_viagem(cidade, dias):
    valor_hotel = custo_hotel(dias)
    valor_aviao = custo_aviao(cidade)
    valor_carro = custo_carro(dias)
    return valor_hotel + valor_aviao + valor_carro


print(custo_viagem("São Paulo", 6))


def custo_viagem_extra(cidade, dias, gastos_extras):
    valor_hotel = custo_hotel(dias)
    valor_aviao = custo_aviao(cidade)
    valor_carro = custo_carro(dias)
    return valor_hotel + valor_aviao + valor_carro + gastos_extras


print(custo_viagem_extra("Manaus", 12, 800))
