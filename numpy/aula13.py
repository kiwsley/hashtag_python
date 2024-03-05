import numpy as np

rng = np.random.default_rng(seed=42)
resposta = rng.integers(low=0, high=10, size=210, endpoint=True)
print(resposta)

notas = np.reshape(resposta,(7,30))

print(notas)

media_geral = np.mean(notas)

print(media_geral)

media_diaria = np.mean(notas, axis=1)

print(media_diaria)