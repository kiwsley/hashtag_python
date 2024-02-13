preco_produto = [ 100,150,300,5500]
produto=['vinho', 'cafeteira','microondas', 'iphone']


impostos=[]
for item in preco_produto:
    impostos.append(item*0.3)

print(impostos)

impostos=[preco *0.3 for preco in preco_produto]
print(impostos)