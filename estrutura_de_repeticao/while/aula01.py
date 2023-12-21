produto = input('registre um produto. Para cancela o registo de um produto, basta aperta enter com a caixa vazia')

vendas =[]

while produto != '':
    vendas.append(produto)
    produto = input('registre um produto. Para cancela o registo de um produto, basta aperta enter com a caixa vazia')





print("registro finalizado. Os produtos cadastrados foram: {}".format(vendas))