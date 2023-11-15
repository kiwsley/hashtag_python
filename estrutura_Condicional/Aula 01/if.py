# condição IF
#enviar um aviso caso o produto bata a meta

meta = 50000
qtda_vendida= 65300

if  qtda_vendida > meta:
    print("Batemos a meta de vendas {} unidades" .format(qtda_vendida))
else:
    print("A meta não foi batida")