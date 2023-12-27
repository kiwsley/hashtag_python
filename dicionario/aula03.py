lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_2tri = {'abril': 88000, 'maio': 89000, 'junho': 120000}

lucro_1tri['abril']=8000

lucro_1tri.update(lucro_2tri)

del lucro_1tri['junho']

print(lucro_1tri)