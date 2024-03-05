import numpy as np

salario=np.array([3000,2500,3500,4000,2000,4500,3000,3800,4800])

media_salarial=np.mean(salario)
print(media_salarial)

print(np.where(salario>media_salarial))
#funcionarios acima da media
print(np.sum(salario>media_salarial))

