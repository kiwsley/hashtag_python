import numpy as np

rng = np.random.default_rng()
print(rng)

numero_aleatorio = int(rng.random()*10)
print(numero_aleatorio)

array_aleatorio = rng.random(3)*100
print(array_aleatorio)

rng = np.random.default_rng(seed=42)

dados_vendas = rng.integers(low=50, high= 200, size=30)
print(dados_vendas)

print(np.max(dados_vendas))
#pegando o indice arg max
print(f"Dia com mais vendas: {np.argmax(dados_vendas)+1}")
print(f"Dia com menos vendas: {np.argmin(dados_vendas)+1}")


#estatisticas

print(np.median(dados_vendas))
print(np.percentile(dados_vendas,50))
print(np.std(dados_vendas))
print(np.var(dados_vendas))