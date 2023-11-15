faturamento = input("Qual foi o faturamento da loja nesse mês?")
custo = input("qual foi o custo da loja nesse mês?")

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print("O lucro da loja foi de R${}".format(lucro))
else:
    print("Preencha o faturamento e o lucro corretamente")