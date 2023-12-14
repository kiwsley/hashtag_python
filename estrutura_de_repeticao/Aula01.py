produtos=['coca','pepsi','guarana','sprite','fanta','agua']
producao=[15000,12000,13000,5000,250,1]

for i in range(len(produtos)):
    print('{} unidades produzidas de {}'. format(producao[i],produtos[i]))