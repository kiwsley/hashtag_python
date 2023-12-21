vendas = []

while True:
    produto = input ("digite o produto: ")
    if not produto:
        break
    qtde = int(input("qual a quantidade? "))
    vendas.append([produto,qtde])

print (vendas)