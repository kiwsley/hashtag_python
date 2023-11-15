# vendas >= 2000 bonus de 15%
# vendas <2000 bonus de 10%
# vendas < 1000 bonus de 0

vendas_funcionario1 = 1000
vendas_funcionario2 = 700
vendas_funcionario3 = 2700


if vendas_funcionario1 >= 1000:
    if vendas_funcionario1 >=2000:
        bonus = vendas_funcionario1*0.15
    else:
        bonus = vendas_funcionario1*0.1
else:
    bonus = 0

print ("O funcionario 1 ganho R$ {}".format(bonus))

if vendas_funcionario2 >= 1000:
    if vendas_funcionario2 >=2000:
        bonus = vendas_funcionario2*0.15
    else:
        bonus = vendas_funcionario2*0.1
else:
    bonus = 0

print ("O funcionario 2 ganho R$ {}".format(bonus))

if vendas_funcionario3 >= 1000:
    if vendas_funcionario3 >=2000:
        bonus = vendas_funcionario3*0.15
    else:
        bonus = vendas_funcionario3*0.1
else:
    bonus = 0

print ("O funcionario 3 ganho R$ {}".format(bonus))