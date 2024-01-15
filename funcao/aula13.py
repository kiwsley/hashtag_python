precos_imoveis = [2.17,1.54,1.45,1.94,2.37,2.3,1.79,1.8,2.25,1.37]
tamanho_imoveis = [207,148,130,203,257,228,160,194,232,147]

fator = 0.1

i = int((1-fator)*len(precos_imoveis))

precos_treino = precos_imoveis[:i]
precos_teste = precos_imoveis[i:]

print(precos_treino)
print(precos_teste)