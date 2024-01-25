#contagem regressiva

import time

for numero in range(10, 0, -1):
    time.sleep(1)
    print("falta {} segundos" .format(numero), end=" \r")

print("Acabou o tempo")