import time

tempo_atual_segundo= time.time()

print(f"tempo atual: {tempo_atual_segundo} segundo desde a Epoch")

inicio = time.time()

for i in range(100_000_000):
    pass
fim = time.time()

print(f"tempo decorrido: {fim-inicio} ")

time.sleep(2)
print("pausa concluída")

tempo_em_segundos = time.time()
tempo_local = time.ctime(tempo_atual_segundo)
print(f"tempo local:{tempo_local}")



tempo_em_segundos = time.time()
tempo_local = time.localtime(tempo_atual_segundo)
print(f"tempo local:{tempo_local}")

print(tempo_local.tm_year)

print(tempo_local.tm_hour)

print(tempo_local.tm_mday)


