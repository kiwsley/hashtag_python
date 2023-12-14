produtos=['apple tv','mac','iphone x','ipad','apple watch','mac book','airpods']
vendas = [1000,1500,15000,270,900,100,1200]

tamanho = len(produtos)
print(tamanho)



print("o produto mais vendidos teve {} unidades vendida". format(max(vendas)))
print("o produto menos vendidos teve {} unidades vendida". format(min(vendas)))

produto_mais_vendido = vendas.index(max(vendas))
produto_menos_vendido = vendas.index(min(vendas))

print("O produto mais vendido: ",produtos[produto_mais_vendido])
print("O produto menos vendido:",produtos[produto_menos_vendido])