from datetime import datetime,timedelta


agora = datetime.now()

print(agora)

print(f"data {agora.date()}")
print(f"data {agora.time()}")

print(f"Ano {agora.year}")
print(f"mes {agora.month}")
print(f"dia {agora.day}")
print(f"hora {agora.hour}")


data_atual = datetime.now()
data_futura = data_atual + timedelta(days=10)

print(f"Data 10 dias no futuro {data_futura}")

#Criando um objeto datetime

data = datetime(2024,5,10,8,30,20)
print(f"data: {data}")


#metdo fromisoformat() = Transforma string em data, porém é preciso seguir o padrão

data_iso = datetime.fromisoformat("2024-01-26 22:00:00")
print(f"data: {data_iso}")

data1= datetime(2024, 1, 2)
data2= datetime(2024, 2, 2)

diferenca= data2 - data1

print(f"a diferença de dias é: {diferenca.days} dias")

if data1 > data2:
    print("primeira data é posterior a data 2")
elif data2> data1:
     print("segunda data é posterior a data 1")
else: 
     print("são iguais")