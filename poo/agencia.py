from random import randint
class Agencia:

    def __init__(self,telefone, cnpj,numero):
        self.telefone = telefone
        self.cnpj =cnpj
        self.numero=numero
        self.cliente=[]
        self.caixa = 0
        self.emprestimo =[]
    
    def verificarCaixa(self):
        if self.caixa < 1000000:
            print("Caixa abaixo do nivel recomendamos. Caixa atual {}".format(self.caixa))
        else:
            print("Caixa ok. Caixa atual {}".format(self.caixa))


    def emprestarDInheiro(self, valor,cpf,juros):
        if self.caixa > valor:
            self.emprestimo.append((valor,cpf,juros))
        else: 
            print("Dinheiro não disponivel")

    def adicionarCliente(self,nome,cpf,patrimonio):
        self.cliente.append((nome,cpf,patrimonio))

class AgenciaVirtual(Agencia):

    def __init__(self, site,telefone,cnpj):
        self.site= site
        super().__init__(telefone,cnpj,1000)
        self.caixa = 1000000
        self.caixaPaypal =0

    def depositalPaypal(self,valor):
        self.caixa -=valor
        self.caixaPaypal +=valor

    def sacarPaypal(self,valor):
        self.caixaPaypal -=valor
        self.caixa+=valor
             

class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj):

        super().__init__(telefone, cnpj, numero =randint(1001,9999))
        self.caixa=1000000
    

class AgenciaPremium(Agencia):
     def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero =randint(1001,9999))
        self.caixa=10000000 
    
     def adicionarCliente(self,nome,cpf,patrimonio):
        if patrimonio > 1000000:
             super().adicionarCliente(nome,cpf,patrimonio)
        else: 
            print("o cliente não tem o patrimonio minimo")
    

agencia1 = Agencia(222,333,444)

agenciavirtual = AgenciaVirtual('virtual.com.br',222,333)
agenciavirtual.verificarCaixa()
agenciavirtual.depositalPaypal(2000)

print(agenciavirtual.caixa)
print(agenciavirtual.caixaPaypal)


agenciaComum = AgenciaComum(555,666)


agenciaPremium = AgenciaPremium(777,888)

agenciaPremium.adicionarCliente('kiw',1500, 1000001)
print(agenciaPremium.cliente)
