import numpy as np

preco = np.array([20,25,30,35,40])

novos_preco = preco *1.1

print(novos_preco)

#np.sum()

vendas = np.array([200,220,250,210,300])

total_vendas = np.sum(vendas)

print(total_vendas)

#np.mean

vendas = np.array([200,220,250,210,300,280,230])

media_vendas = np.mean(vendas)

print(media_vendas)

#np.max np.min

vendas = np.array([199,200,220,250,210,300,280,230])
maior_venda=np.max(vendas)
menor_venda=np.min(vendas)

print(maior_venda, menor_venda)

#np.sort

vendas = np.array([199,200,220,250,210,300,280,230])
sorte=np.sort(vendas)

print(sorte)

#np.dot()

quantidade = np.array([10,20,30,40])
preco= np.array([5,10,15,20])

#calcular a vendas e soma o array

print(np.dot(quantidade,preco))

