vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

itens_dicionarios = vendas_tecnologia.items()

for produto, qtde in itens_dicionarios:
    print('{} {} unidades'.format(produto, qtde))
print()
for chave in vendas_tecnologia:
    if vendas_tecnologia[chave] > 5000:
        print('{} {} unidades'.format(chave, vendas_tecnologia[chave]))
