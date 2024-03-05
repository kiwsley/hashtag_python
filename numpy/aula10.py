import numpy as np

vendas = np.array([200,220,250,210,300,280,230,210,220,240,230,210,280,220])
#reoganizar os dados em matriz de 2x7
vendas_reshaped = np.reshape(vendas,(2,7))

print(vendas_reshaped)
#quantidade de dimensões
print(vendas.ndim)
#numero de elementos
print(vendas.shape)

print(vendas_reshaped[0])

print(vendas_reshaped[1])

#soma do eixos

print (vendas_reshaped.sum(axis=0))
print (vendas_reshaped.sum(axis=1))