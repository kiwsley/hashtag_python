import numpy as np
import time

array = np.array([1,2,3,4,5])

lista = [1, "dois", 3.0]

novo_array = array + 1
print(novo_array)

#-------------- Eficiencia do numpy------------

lista = list(range(1, 10_000_001))
array = np.array(range(1, 10_000_001))

# calcula a soma de todos os numero da lista

inicio = time.time()
soma_lista=sum(lista)
fim = time.time()
print(f"Tempo para somar todos os numeros na lista: {fim-inicio} segundos (LISTA)")


# calcula a soma de todos os numero no array

inicio = time.time()
soma_array=np.sum(array)
fim = time.time()
print(f"Tempo para somar todos os numeros na lista: {fim-inicio} segundos (ARRAY)")

