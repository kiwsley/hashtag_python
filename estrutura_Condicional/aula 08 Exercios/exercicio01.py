produto = input("Qual o Produto?")
categoria = input ("Qual a Categoria?")
qtde = int(input("Qual a Quantidade?"))

if produto and categoria and qtde:
    if categoria == 'bebidas':
        if qtde < 75:
            print("Solicitar {} à equipe de compras, temos apenas {} unidades".format(produto,qtde))
else:
    print("Preencha todas as informações?")