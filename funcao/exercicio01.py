def carga_tributaria(preco, custo, lucro):
    imposto = preco- custo-lucro
    carga = imposto/preco * 100
    return carga

preco = 1500
custo = 400
lucro= 800

print("A carga de tributo foi {}% ".format(carga_tributaria(preco,custo,lucro)))