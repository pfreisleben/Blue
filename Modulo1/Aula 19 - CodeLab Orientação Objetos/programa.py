from classeBomba import bombaCombustivel

etanol = bombaCombustivel("etanol", 3.5, 1000)
gasolina = bombaCombustivel("gasolina", 4.98, 1000)
diesel = bombaCombustivel("diesel", 5.00, 1000)

while True:
    print(f'1 - Abastecer por valor')
    print(f'2 - Abastecer por litro')
    print(f'3 - Alterar valor do litro do combustivel')
    print(f'4 - Alterar o tipo de combustivel')
    print(f'5 - Alterar quantidade disponivel de combustivel')
    opcao = input("Digite sua opção: ")
    if opcao == '1':
        print(f'Combustiveis disponiveis: etanol, gasolina e diesel.')
        escolha = input("Digite o nome do tipo de combustivel escolhido: ")
        if escolha == "gasolina":
            gasolina.abastecerPorValor()
        elif escolha == "etanol":
            etanol.abastecerPorValor()
        elif escolha == "diesel":
            diesel.abastecerPorValor()
        else:
            print(f'Opção inválida.')
            continue
    elif opcao == '2':
        print(f'Combustiveis disponiveis: etanol, gasolina e diesel.')
        escolha = input("Digite o nome do tipo de combustivel escolhido: ")
        if escolha == "gasolina":
            gasolina.abastecerPorLitro()
        elif escolha == "etanol":
            etanol.abastecerPorLitro()
        elif escolha == "diesel":
            diesel.abastecerPorLitro()
        else:
            print(f'Opção inválida.')
            continue
    elif opcao == '3':
        print(f'Combustiveis disponiveis: etanol, gasolina e diesel.')
        escolha = input("Digite o nome do tipo de combustivel escolhido: ")
        if escolha == "gasolina":
            gasolina.alterarValor()
        elif escolha == "etanol":
            etanol.alterarValor()
        elif escolha == "diesel":
            diesel.alterarValor()
        else:
            print(f'Opção inválida.')
            continue
    elif opcao == '4':
        print(f'Combustiveis disponiveis: etanol, gasolina e diesel.')
        escolha = input("Digite o nome do tipo de combustivel escolhido: ")
        if escolha == "gasolina":
            gasolina.alterarCombustivel()
        elif escolha == "etanol":
            etanol.alterarCombustivel()
        elif escolha == "diesel":
            diesel.alterarCombustivel()
        else:
            print(f'Opção inválida.')
            continue
    elif opcao == '5':
        print(f'Combustiveis disponiveis: etanol, gasolina e diesel.')
        escolha = input("Digite o nome do tipo de combustivel escolhido: ")
        if escolha == "gasolina":
            gasolina.alterarQuantidadeCombustivel()
        elif escolha == "etanol":
            etanol.alterarQuantidadeCombustivel()
        elif escolha == "diesel":
            diesel.alterarQuantidadeCombustivel()
        else:
            print(f'Opção inválida.')
            continue
    else:
        print(f'Opção inválida!')
