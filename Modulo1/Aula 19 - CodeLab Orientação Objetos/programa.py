from classeBomba import bombaCombustivel

tipo = input("Digite o tipo de combustivel: ")
valor = float(input("Digite o valor por litro do combustivel: "))
qtdLitros = float(
    input("Informe a quantidade de litros disponivel no posto: "))
bomba = bombaCombustivel(tipo, valor, qtdLitros)

while True:
    print(bomba)
    print(f'1 - Abastecer por valor')
    print(f'2 - Abastecer por litro')
    print(f'3 - Alterar valor do litro do combustivel')
    print(f'4 - Alterar o tipo de combustivel')
    print(f'5 - Alterar quantidade disponivel de combustivel')
    opcao = input("Digite sua opção: ")
    if opcao == '1':
        bomba.abastecerPorValor()
    elif opcao == '2':
        bomba.abastecerPorLitro()
    elif opcao == '3':
        bomba.alterarValor()
    elif opcao == '4':
        bomba.alterarCombustivel()
    elif opcao == '5':
        bomba.alterarQuantidadeCombustivel()
    else:
        print(f'Opção inválida!')
