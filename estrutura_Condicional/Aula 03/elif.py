#Validar os bonus para um funcionário

meta_vendas = 20000
vendas= 25000

if vendas < meta_vendas: 
    print("Não ganhou bonus")
elif vendas > (2*meta_vendas):
    bonus = 0.07* vendas
    print("Ganhou R$ {} de bônus".format(bonus))
else:
    bonus = 0.03* vendas
    print("Ganhou R$ {} de bônus".format(bonus))