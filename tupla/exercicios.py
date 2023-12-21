meta = 10000
vendas= [
    ('joao', 15000),
    ('julia', 27000),
    ('Marcus', 9900),
    ('maria', 3750),
    ('ana', 10300),
    ('Alon',7870)
]

for vendedor, qtde in vendas:
    if qtde >=meta:
        print('{} bateu a meta, vendeu {} unidades'.format(vendedor,qtde))
