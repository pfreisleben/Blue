""" Crie um programa, utilizando dicionário, que simule a baixa de estoque das vendas
de um supermercado. Não esqueça de fazer as seguintes validações:
estoque = {"tomate": [1000, 2.30], "alface": [500, 0.45], "batata": [2001, 1.20],
"feijão": [100, 1.50]}
Produto Indisponível
Produto Inválido
Quantidade solicitada não disponível
O programa deverá mostrar para o cliente a quantidade de itens comprados e o total a
pagar. """
estoque = {"tomate": [1000, 2.30], "alface": [500, 0.45], "batata": [2001, 1.20],
           "feijao": [100, 1.50]}
compra = {}

while True:
    nomeProduto = input(
        "Digite o nome do produto que deseja comprar ou 0 para sair: ").lower()
    if nomeProduto in estoque.keys():
        produto = estoque.get(nomeProduto)
    elif nomeProduto == '0':
        break
    else:
        print("Esse produto não existe em nossa loja!")
        continue
    print(f'O preço do produto é: R$ {produto[1]}')
    print(f'Estoque disponivel: {produto[0]}')
    qtdSelecionada = int(input("Agora, digite a quantidade desejada: "))
    while qtdSelecionada > produto[0]:
        print(f'A quantidade selecionada é maior do que a quantidade disponivel, tente novamente.')
        qtdSelecionada = int(input("Agora, digite a quantidade desejada: "))
    # Faz a baixa do saldo no estoque
    estoque.update({nomeProduto: [produto[0]-qtdSelecionada, produto[1]]})
    if nomeProduto in compra.keys():
        qtdAtual = compra.get(nomeProduto)
        compra.update({nomeProduto: [qtdAtual[0]+qtdSelecionada,
                      produto[1], (qtdAtual[0]+qtdSelecionada)*produto[1]]})
    else:
        compra.update(
            {nomeProduto: [qtdSelecionada, produto[1], qtdSelecionada*produto[1]]})
totalCompra = 0
print(f'O resumo da sua compra:')
for k, v in compra.items():
    print(
        f'Produto: {k} - Quantiade: {v[0]} - Preço: {v[1]} - Total: R${v[2]}')
    totalCompra += v[2]
print(f'Total a pagar: R$ {totalCompra}')

print(f'Como ficou o nosso estoque: ')
for k, v in estoque.items():
    print(
        f'Produto: {k} - Estoque restante: {v[0]} - Preço: {v[1]}')
