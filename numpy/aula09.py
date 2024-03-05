import numpy as np
#ciclo de produção +2 e -2 (Desvio padrão)
tempos_ciclo = np.array([5.5, 5.7, 5.9, 6.0, 5.8, 5.6, 5.7, 7.2, 4.8])
media = np.mean(tempos_ciclo)
print(media)


desvio_padrao = np.std(tempos_ciclo)
print(desvio_padrao)
#verificando anomalias
condicao = (tempos_ciclo > media + 2* desvio_padrao) | (tempos_ciclo<media -2* desvio_padrao)
anomalias = np.where(condicao)
print(anomalias)

print(tempos_ciclo[anomalias])

print(f"Os tempos que estão na condição pedida são: {tempos_ciclo[condicao]}")