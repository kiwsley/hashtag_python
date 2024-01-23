import time
import locale

#link https://docs.python.org/3/library/time.html#time.strftime
locale.setlocale(locale.LC_TIME, 'pt_br.UTF-8')

tempo_em_struct = time.localtime()
print(tempo_em_struct)

print(time.strftime("%d,%B,%Y", tempo_em_struct))

#time.strptime()

string_tempo = '30 junho, 2023'
formato= "%d %B, %Y"
tempo_em_struct = time.strptime(string_tempo,formato)

print(f"tempo em struct:{tempo_em_struct}")

#time.gmtime()

time.gmtime(0)
gmt_struct=time.gmtime()
print(gmt_struct)