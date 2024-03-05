import numpy as np

dados =[127,90,201,150,210,220,115]

vendas = np.array(dados)

media_vendas = np.mean(vendas)

print(media_vendas)

precos= np.array([31.4,31.25,30.95,31.20, 31.6,31.5])

precos_maximo = np.max(precos)
precos_minimo = np.min(precos)

print(precos_maximo)
print(precos_minimo)

variacao_preco = precos_maximo - precos_minimo

print(variacao_preco)


quantidades = np.array([5,3,2])
preco2 = np.array([100,200,50])
#só é possivel por conta da biblioteca numpy
print(quantidades*preco2)

print(np.sum(quantidades*preco2))

#funcao dot
print(np.dot(quantidades,preco2))