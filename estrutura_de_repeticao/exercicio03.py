meta = 10000
vendas = [
    ['joao', 15000],
    ['julia', 27000],
    ['marcus', 9900],
    ['maria', 3750],
    ['ana', 10300],
    ['alon', 7870]
]

#criando lista auxilia

acima_meta =[]

for venda in vendas:
    if venda[1]>=meta:
        acima_meta.append(venda)

print (acima_meta)

print('{:.1%} dos vendedores bateram a meta'.format(len(acima_meta)/len(vendas)))

melhor_vendedor =''
mais_vendeu = 0

for venda in vendas:
    if venda[1]>mais_vendeu:
        mais_vendeu=venda[1]
        melhor_vendedor = venda[0]

print(melhor_vendedor,mais_vendeu)