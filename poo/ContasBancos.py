class ContaCorrente:

    def __init__(self,nome,cpf):
        self.nome=nome
        self.cpf=cpf
        self.saldo = 0

    def ConsultarSaldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self.saldo))


    def depositar(self,valor):
        self.saldo+=valor
        pass


    def sacarDinheiro(self,valor):
        self.saldo-=valor
        pass


contaKiw=ContaCorrente("kiw","12345")
contaKiw.depositar(20)
print(contaKiw.saldo)
print(contaKiw.cpf)
contaKiw.ConsultarSaldo()
contaKiw.sacarDinheiro(10)
contaKiw.ConsultarSaldo()