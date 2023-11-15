# Criar um progrma que calcule e dê um print no bonus que os funcionarios devem receber

# Se o valor for maior que a meta, o valor do bonus do funcionario é 10%
#meta 1000 vendas
meta = 1000
vendas_funcionario1 = 1000
vendas_funcionario2 = 700
vendas_funcionario3 = 2700

if vendas_funcionario1 >= meta:
    bonus1 = vendas_funcionario1 * 0.1
else:
    bonus1 = 0
if vendas_funcionario2 >= meta:
    bonus2 = vendas_funcionario2 * 0.1
else:
    bonus2 = 0
if vendas_funcionario3 >= meta:
   bonus3 = vendas_funcionario3 * 0.1
else:
    bonus3 = 0

print("O funcionario 1 ganhou R${}".format(bonus1))
print("O funcionario 2 ganhou R${}".format(bonus2))
print("O funcionario 3 ganhou R${}".format(bonus3))