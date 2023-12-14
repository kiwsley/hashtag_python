vendedores = ['lira','joao','Diego','Alon']
lista =["mac","iphone"]
vendas =[
    [100,200],
    [300,500],
    [50,1000],
    [900,10],
]

vendas_ipad_joao = vendas[1][0]
print(vendas_ipad_joao)

vendas_iphone_diego= vendas[2][1]
print(vendas_iphone_diego)

vendas_iphone= vendas[0][1]+vendas[1][1]+vendas[2][1]+vendas[3][1]
print(vendas_iphone)

vendas[0][1] = 50

print (vendas)

vendas_mac=[10,15,6,70]

vendas[0].append(vendas_mac[0])
vendas[1].append(vendas_mac[1])
vendas[2].append(vendas_mac[2])
vendas[3].append(vendas_mac[3])
print ("vendas atualizadas:{}" .format(vendas))
