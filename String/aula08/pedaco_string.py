#forma basica

precos="jan: 25, fev: 27, mar:29"
preco_jan=precos[5:7]
print(preco_jan)

#posição final

preco_mar = precos[-2:]
print (preco_mar)
 
preco_fev = precos[14:16]
print(preco_fev)

#Posição inicial e final com step

codigo= '1.2.3.4,5,1,2.3.4,7.9'

pedaco_cod = codigo[::-1]
print (pedaco_cod)