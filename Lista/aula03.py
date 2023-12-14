produtos=['tv','celular','tablet','mouse','teclado','geladeira','forno']
estoque = [100,150,100,120,70,190,80]

i = produtos.index('geladeira')

print(produtos[i])
print(estoque[i])

produto = input("Insira o nome do produto: ")

if produto in produtos:
    i = produtos.index(produto)
    print (i)
    qtde_estoque=estoque[i]
    print('temos {} unidades de {} no estoque'.format(qtde_estoque,produto))
else:
    print("nome do produto {} não existe no estoque".format(produto))