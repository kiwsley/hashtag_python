

class TV:
    cor='preta'

    def __init__(self,tamanho):        
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "netflix"
        self.volume = 10

    def mudar_canal(self,canal):
        self.canal = canal

tv_sala=TV(tamanho=55)
tv_quarto = TV(tamanho=15)

tv_sala.mudar_canal('amazon prime')

TV.cor='branca'

print(tv_sala.canal)
print(tv_quarto.canal)

print(tv_sala.tamanho)
print(tv_quarto.tamanho)

print(tv_sala.cor)
print(tv_quarto.cor)