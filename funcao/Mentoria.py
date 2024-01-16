#calcular quantas latas custa comprar a tinta
    #descobrir a area a ser pintada

area = float(input("Qual a area(m²) a ser pintada? "))
    #quantos litros de tinta o cliente precisa
litros= area/6
    #quanta latas vou precisar
    #arredondar numero   
latas = litros/18
if int(latas)!= latas:
    latas = int(latas)+1
    #calcular o preço das latas
preco = latas*80

print("quantidade de latas ", latas)
print("preço", preco)


area = float(input("Qual a area(m²) a ser pintada? "))
    #quantos litros de tinta o cliente precisa
litros_tinta= area/6
    #quanta latas vou precisar
    #arredondar numero   
if litros_tinta % 3.6 > 0:
    galoes = int(litros_tinta/3.6)+1
else:
    galoes=litros_tinta / 3.6

    #calcular o preço das latas
preco = galoes*25

print("quantidade de Galões ", galoes)
print("preço", preco)

