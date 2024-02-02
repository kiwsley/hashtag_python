import matplotlib.pyplot as plt
#importando o módulo numpy
import numpy as np

vendas = np.random.randint(10, 3000, 50)
meses = np.arange(1, 51)
print(meses)

plt.plot(meses, vendas, 'r--')
plt.axis([0, 50, 0, max(vendas)+100])
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.show()