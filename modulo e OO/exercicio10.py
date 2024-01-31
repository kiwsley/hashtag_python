#oferecer desconto para cliente com base na ultima compra

from datetime import datetime

ultima_compra = datetime(2024,1,10)

data_hora_atual = datetime.now()

print(ultima_compra)
print(data_hora_atual)

diferenca= data_hora_atual- ultima_compra

print(diferenca)

print(diferenca.days)

if(diferenca.days > 30):
    print("você ganhou uma desconto!!")
else:
    print("NÃO ganhou desconto!")



