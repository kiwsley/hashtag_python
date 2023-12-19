qtde_pessoas= int(input("quantas pessoas terão no quarto? "))


quarto=[]

for i in range(qtde_pessoas):
    nome = input('qual o nome? ')
    cpf= input("qual CPF? ")
    hospede = [nome,'CPF:{}'.format(cpf)]
    quarto.append(hospede)
print(quarto)




