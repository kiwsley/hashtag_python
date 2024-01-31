from datetime import datetime
from zoneinfo import ZoneInfo

def verifica_horario(data_hora):
    if 9 <= data_hora.hour <17:
        return " Aberto"
    else:
        return "Fechado"

data_hora_atual = datetime.now()

print(data_hora_atual)

fuso_horario_SP= ZoneInfo("America/Sao_Paulo")
fuso_horario_NY= ZoneInfo("America/New_York")
fuso_horario_TK= ZoneInfo("Asia/Tokyo")

data_hora_SP=data_hora_atual.astimezone(fuso_horario_SP)
data_hora_NY=data_hora_atual.astimezone(fuso_horario_NY)
data_hora_TK=data_hora_atual.astimezone(fuso_horario_TK)

print (data_hora_SP)
print (data_hora_NY)
print (data_hora_TK)


    
print(f"O escritorio de São paulo está {verifica_horario(data_hora_SP)}")  
print(f"O escritorio de New York está {verifica_horario(data_hora_NY)}")  
print(f"O escritorio de Tokio está {verifica_horario(data_hora_TK)}")   