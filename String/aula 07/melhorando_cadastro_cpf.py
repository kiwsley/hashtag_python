cpf = input('Insira seu CPF: ')

#tratar CPF 
#tirar espaços
cpf=cpf.strip()
#tirar pontos 
cpf = cpf.replace('.','')
#tirar traços
cpf = cpf.replace('-','')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('Insira seu CPF corretamente(Digite apenas número)')