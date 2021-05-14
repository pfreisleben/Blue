""" ThisO Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 
1,99 e agora possui uma loja de conveniências. Faça um programa que implemente 
uma caixa registradora rudimentar. O programa deverá receber um número 
desconhecido de valores referentes aos preços das mercadorias. Um valor zero 
deve ser informado pelo operador para indicar o final da compra. O programa deve
 então mostrar o total da compra e perguntar o valor em dinheiro que o cliente 
 forneceu, para então calcular e mostrar o valor do troco. Após esta operação, 
 o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
 A saída deve ser conforme o exemplo abaixo:"""

while True:
    vlrProdutos = []
    print("Olá, vamos iniciar o registro dos itens.")
    for produto in range(1, 1000):
        valor = float(
            input(f'Digite o valor do produto {produto}, ou digite 0 para terminar. '))
        if valor == 0:
            break
        else:
            vlrProdutos.append(valor)
    print(f'Total da compra: R${sum(vlrProdutos)}')
    dinheiro = float(
        input("Informe o valor em dinheiro que o cliente forneceu: "))
    print(f'Troco: {dinheiro-sum(vlrProdutos)}')
    print("Iniciando nova compra...")
