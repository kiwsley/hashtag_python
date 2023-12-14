produtos=['apple tv','mac','iphone x','ipad','apple watch','mac book','airpods']

#adicionar

produtos.append('iphone 11')
print(produtos)
#remover iphone x

#produtos.remove('iphone x')
#print(produtos)

produtos.pop(2)
print(produtos)


#produtos_remover ='iphone11'
#if produtos_remover in produtos:
#    produtos.remove('iphone11')
#else:
#    print("não existe na lista de produtos")

try:
    produtos.remove('iphone 11')
    print(produtos)
except:
    print("não existe na lista de produtos")




