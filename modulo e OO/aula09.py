from datetime import datetime , timedelta,timezone
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

agora = datetime.now()
print(agora)

print(type(agora))

print(agora.strftime("%A,%d"))

# modulo strptime()
string_data ="30 Junho, 2023, 15:30:20"
formato = "%d %B, %Y, %H:%M:%S"

data = datetime.strptime(string_data,formato)

print(f"data: {data}")

#fuso horario

fuso_horario = timezone.utc
data_hora = datetime(2023,6,26,15,30,20, tzinfo=fuso_horario)
print(f"Data/hora {data_hora}")

#fuso horario sao paulo

fuso_horario_SP = timezone(timedelta(hours=-3))
data_hora_SP = datetime(2023,6,26,15,30,20, tzinfo=fuso_horario_SP)
print(f"Data/hora sao paulo: {data_hora_SP}")

from zoneinfo import ZoneInfo

fuso_SP = ZoneInfo('America/Sao_Paulo')
data_hora = datetime(2023,6,26,15,30,20, tzinfo=fuso_SP)
print(f"Data/hora {data_hora}")


#Conversão de fuso horario

data_hora_atual = datetime.now()


fuso_horario_NY = ZoneInfo('America/New_York')
data_hora_new_york= data_hora_atual.astimezone(fuso_horario_NY)

print(f"Fuso horarios atual em New York: {data_hora_new_york}")