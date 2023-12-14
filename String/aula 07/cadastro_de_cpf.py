cpf = input('Insira seu CPF(Digite apenas número)')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('Insira seu CPF corretamente(Digite apenas número)')