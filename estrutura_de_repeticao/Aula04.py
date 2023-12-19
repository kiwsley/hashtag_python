funcionarios=['maria','jose','antonio','joao','francisco']

for i, item in enumerate(funcionarios):
    print('{} é o funcionario: {}'.format(i, item))

estoque=[1220,300,800,1500,1990,2750,40,20,23]
produtos=['coca','pepsi', 'guarana','skol','brahma','agua','del vale','dolly','red bull']
nivel_minimo=50

for i, qtde in enumerate(estoque):
    if qtde < nivel_minimo:
        print('{} está abaixo do nivel minimo. Temos apenas {}'.format(produtos[i],qtde))