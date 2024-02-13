vendas_produto = [ 1500,150,2100,1950]
produto=['vinho', 'cafeteira','microondas', 'iphone']

lista_aux = list(zip(vendas_produto, produto))
print(lista_aux)

lista_aux.sort(reverse=True)
print(lista_aux)

produto=[produto for vendas, produto in lista_aux]
print(produto)