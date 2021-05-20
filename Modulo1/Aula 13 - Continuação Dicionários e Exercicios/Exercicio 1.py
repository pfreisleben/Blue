""" Crie um programa onde você cadastre a data de nascimento (dd/mm/aa) de algumas
celebridades em um dicionário. Ao escolher uma celebridade, seu programa deve
retornar a data completa. Não esqueça de validar se a celebridade escolhida está
presente em seu dicionário """
cadastra = True
celebridades = {}
while cadastra:
    nome = input("Digite o nome da celebridade: ").lower()
    nascimento = input("Informe a data de nascimento(dd/mm/aa): ")
    continua = print(
        f'Gostaria de cadastrar uma nova celebridade? S/N ').lower()
    if continua == "n":
        cadastra = False
escola = input("Agora, digite o nome da celebridade que deseja consultar: ")
