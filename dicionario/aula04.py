vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

for chave in vendas_tecnologia:
    print('{}: {} Unidades '.format(chave, vendas_tecnologia[chave]))

total_notebook = 0

for chave in vendas_tecnologia:
    if 'notebook' in chave:
        total_notebook+= vendas_tecnologia[chave]

print(total_notebook)