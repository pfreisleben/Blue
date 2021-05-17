""" ThisO Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 
1,99 e agora possui uma loja de conveniências. Faça um programa que implemente 
uma caixa registradora rudimentar. O programa deverá receber um número 
desconhecido de valores referentes aos preços das mercadorias. Um valor zero 
deve ser informado pelo operador para indicar o final da compra. O programa deve
 então mostrar o total da compra e perguntar o valor em dinheiro que o cliente 
 forneceu, para então calcular e mostrar o valor do troco. Após esta operação, 
 o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
 A saída deve ser conforme o exemplo abaixo:"""


while True:  # Repetição sempre irá rodar, pois a condição será sempre True.
    print("Bem-vindo, vamos iniciar o registro da compra! ")
    lista1 = []  # Lista usada para receber o nome do produto
    lista2 = []  # Lista para receber os preços inseridos
    # Essa variável vai ser utilizada para checar se o programa deverá registrar novos itens ou não.
    registraItem = True
    while registraItem:  # Caso registraItem == True, rode:
        produto = input("Informe o produto, ou digite 0 para terminar: ")
        if produto == "0":
            print(f'Encerrando registro dos itens...')
            # Faz a variavel registraItem ser False, para que não peça novos itens
            registraItem = False
            break
        else:
            preco = float(input("Informe o valor que vai pagar em dinheiro: ").replace(
                ',', '.'))  # Recebe preço do produto
            lista1.append(produto)  # Insere o nome na lista.
            lista2.append(preco)  # Insere o preço na lista.
    # A função sum(list) faz a soma dos valores dentro da lista
    print(f'Total da compra: R${sum(lista2)}')
    dinheiro = float(input("Digite o valor pago pelo cliente: "))
    print(f'O troco que deverá ser dado: R${dinheiro - sum(lista2)}')
