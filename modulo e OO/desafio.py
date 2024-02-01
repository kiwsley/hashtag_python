from datetime import datetime


data_nacimento=input("Digite sua data de nascimento (dd/mm/aaaa): ")

data_nacimento = datetime.strptime(data_nacimento,"%d/%m/%Y")

data_atual = datetime.now()

idade_user= data_atual.year - data_nacimento.year

mes_atual = data_atual.month
dia_atual = data_atual.day

mes_nascimento = data_nacimento.month
dia_nascimento = data_nacimento.day

if mes_nascimento>mes_atual:
    idade_user -=1
elif mes_nascimento == mes_atual and dia_nascimento > dia_atual:
    idade_user -=1

print(idade_user)