import numpy as np

salario = np.array([3000,3500,4000,2000,4500,4000,5000])

media_salarial = np.mean(salario)

print(media_salarial)


funcionario_acima_media = np.where(salario > media_salarial)
print(funcionario_acima_media)

print(salario[funcionario_acima_media])


print(np.where(salario> media_salarial, "Acima da média","Abaixo da media"))

salario_bonus = np.where(salario< media_salarial, salario*1.1, salario)
print(salario_bonus)

print(np.where((salario>=3000)&(salario <=4500)))