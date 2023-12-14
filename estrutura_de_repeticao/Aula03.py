vendas = [1200,300,800,1500,1900,2750,4000,20,23,70,90,80,1100,999,900]
meta = 1000

qtda_bateu_meta = 0

for venda in vendas:
    if venda >=meta:
        qtda_bateu_meta+=1
        
print("Quantidade de funcionário que bateram a meta: {}".format(qtda_bateu_meta))
