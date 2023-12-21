vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]
faturamento = 0
produto_mais_vendido = ''
unidades_mais_vendida =0

for item in vendas:
    data,produto,cor,capacidade,unidades,valor_unitario = item
    if produto == 'iphone x' and data =='20/08/2020':
        faturamento+= unidades*valor_unitario
    if data =='21/08/2020':
        if unidades > unidades_mais_vendida:
            produto_mais_vendido = produto
            unidades_mais_vendida = unidades

print('O faturamento de Iphone no dia 20/08/2023 foi de {}'.format(faturamento))
print(produto_mais_vendido, unidades_mais_vendida)
