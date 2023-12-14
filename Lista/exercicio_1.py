meses=['jan','fev','mar','abr','mai','jun','jul','ago','set','out', 'nov','dez']
vendas_1sem = [25000,29000,22200,17750,15870,19900]
vendas_2sem = [19850,20120,17540,15555,49051,9650]


vendas_1sem.extend(vendas_2sem)

maior_valor = max (vendas_1sem)
menor_valor = min (vendas_1sem)
print("maior valor: {}".format(maior_valor))
print("maior valor: {}".format(menor_valor))


print(vendas_1sem)

i_maior_valor=vendas_1sem.index(maior_valor)
i_menor_valor=vendas_1sem.index(menor_valor)

print (i_maior_valor)
print (i_menor_valor)

print("o melhor mês do ano foi {} com {} vendas" .format(meses[i_maior_valor], maior_valor))
print("o pior mês do ano foi {} com {} vendas" .format(meses[i_menor_valor], menor_valor))

faturamento_total= sum(vendas_1sem)

print("faturamento total: {}".format(faturamento_total))

percentual = (maior_valor/faturamento_total)
print("o melhor mês representou {:.2%} das vendas". format(percentual))


print("------top 3-------")
top3= []
print(vendas_1sem)
maior_valor = max(vendas_1sem)
top3.append(maior_valor)
print(top3)
vendas_1sem.remove(maior_valor)
print(vendas_1sem)
maior_valor = max(vendas_1sem)
top3.append(maior_valor)
print(top3)
vendas_1sem.remove(maior_valor)
maior_valor = max(vendas_1sem)
top3.append(maior_valor)
print(top3)