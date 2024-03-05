import numpy as np

vendas = np.array([[50,60,70,65,80],
                   [85,90,78,92,88],
                   [72,75,68,77,76]])

vendas_produto = np.sum(vendas, axis=1)
print(vendas_produto)
vendas_dia = np.sum(vendas, axis=0)
print(vendas_dia)