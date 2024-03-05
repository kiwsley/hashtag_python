import numpy as np

rng = np.random.default_rng(seed=42)
vendas=rng.integers(low=20, high=200,size=30, endpoint=True)

print(vendas)

vendas_semanais= np.reshape(vendas,(5,6))
print(vendas_semanais)

print(vendas_semanais.sum(axis=1))
print(vendas_semanais.mean(axis=1))
print(vendas_semanais.mean(axis=0))
