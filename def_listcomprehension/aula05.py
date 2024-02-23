def calcular_imposto(imposto):
    return lambda preco: preco *(1+ imposto)

calcular_preco_produto = calcular_imposto(0.1)
calcular_preco_servico = calcular_imposto(0.15)
calcular_preco_royalties = calcular_imposto(0.25)

print (calcular_preco_produto(100))