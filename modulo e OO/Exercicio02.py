#Formatação de data e hora
import time
import locale

locale.setlocale(locale.LC_TIME, 'pt_br.UTF-8')

tempo_em_struct = time.localtime()


print(tempo_em_struct)


tempo_formatado = time.strftime("%A, %d de %B %Y, %H:%M", tempo_em_struct)

print(tempo_formatado)