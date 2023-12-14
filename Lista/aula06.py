#juntar listas, ordenas e cuidados especiais

produtos=['apple tv','mac','iphone x','ipad','apple watch','mac book','airpods']
novos_produtos=['iphone 12','ioculos']

produtos.extend(novos_produtos)
todos_produtos = produtos+novos_produtos

print(produtos)
print(todos_produtos)

#ordenação
produtos.sort()
print(produtos)