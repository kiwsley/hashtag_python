meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}

def calcular_meta(meta,venda):
    bateram_meta = []
    for vendedor in vendas:
        if vendas[vendedor]> meta:
            bateram_meta.append(vendedor)
    percentual_meta = len(bateram_meta)/len(vendas)    

    return percentual_meta, bateram_meta

print(calcular_meta(meta,vendas))