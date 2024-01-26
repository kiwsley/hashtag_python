import time

tempo_atual = time.localtime()

print(tempo_atual.tm_year)

tempo_ano_novo = (tempo_atual.tm_year +1, 1,1, 0, 0, 0, 0, 0, 0,)
print(tempo_ano_novo)

print(time.mktime(tempo_atual))
print(time.mktime(tempo_ano_novo))

segundo_restantes=int(time.mktime(tempo_ano_novo)-time.mktime(tempo_atual))
print(segundo_restantes)

segundo_por_minuto=60
segundos_por_hora = 60*60
segundos_por_dia =24*60*60

resultado, resto = divmod(130,segundo_por_minuto)

dias, resto_segundos=divmod(segundo_restantes, segundos_por_dia)
print(dias)
print(resto_segundos)

horas, resto_segundos=divmod(resto_segundos,segundos_por_hora)
minutos, segundos = divmod(resto_segundos,segundo_por_minuto)

print(horas)
print(minutos)
print(segundos)

print(f"Falta{dias}, {horas} horas, {minutos} minutos e {segundos} segundos para o ano novo!!! ")


