#calcula o menor preço possivel de latas e galoes para pintar uma parede
    #decobrir a area a ser pintada
area = float(input("Qual a area(m²) a ser pintada? "))
    #calcular quantas litros vamos precisar
litro = area/6
    #calcular quantas latas e galoes vamos precisar

        #calcular quantas latas inteiras vamos precisar
latas = int(litro/18)
        #calcular quanto vai sobrar de litros de tintas
litros_faltam = litro % 18
        #se sobra tinta:

            #quantos galoes vamos precisar para essa sobra
if litros_faltam>0:
    if litros_faltam /3.6 > 0:
        galoes = int(litros_faltam / 3.6)+1
    else:
        galoes = litros_faltam / 3.6


    #calcular o preço
        #quant latas inteirar * 80
preco_lata = latas * 80
        #se qtde_ galoes *25 > 80

            #preco anterior + 80
        #caso contrario
            #preco anterior + qtd *25
preco_galoes = galoes *25
if preco_galoes > 80:
    latas = latas +1
    preco_lata = latas *80
    galoes = 0
    preco_galoes = 0
    
preco_final = preco_lata + preco_galoes

print("Latas: ", latas)
print("Galoes: ", galoes)
print("Preço final: ", preco_final)