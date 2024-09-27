from datetime import datetime
import pytz
import time
from random import randint

class ContaCorrente:

    """
    Atributos: descrever todos os atributos de acordo com a a PEP 257

    """

    @staticmethod
    def _dataHora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S')


    def __init__(self,nome,cpf,agencia,numConta):
        self._nome=nome
        self._cpf=cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self.numConta = numConta
        self._transacoes = []
        self.cartoes=[]

    def ConsultarSaldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self._saldo))
        

    def depositar(self,valor):
        self._saldo+=valor
        self.ConsultarSaldo()
        self._transacoes.append((valor, self._saldo,ContaCorrente._dataHora()))

    
    def _limiteConta(self):
        #como fosse o limite especial
        self._limite = -1000
        return self._limite
    

    def consultarLimiteChequeEspecial(self):
        print("Seu limite do cheque especial é {:,.2f}".format(self._limiteConta()))
        


    def sacarDinheiro(self,valor):
        if self._saldo - valor < self._limiteConta():
            print("Saldo insuficiente")
            self.ConsultarSaldo()

        else:
            self._saldo-=valor
            self._transacoes.append((-valor, self._saldo,ContaCorrente._dataHora()))
    

    def consultaHistorico(self):
        print("\nHistorico da conta: \n")

        for transacao in self._transacoes:
            print(transacao)


    def transferir(self, valor, contaDestino):
        self._saldo-=valor
        self._transacoes.append((-valor, self._saldo,ContaCorrente._dataHora()))
        contaDestino._saldo +=valor
        contaDestino._transacoes.append((valor, contaDestino._saldo,ContaCorrente._dataHora()))

class CartaoCredito:

    @staticmethod
    def _dataHora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br#.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self,titular,conta_corrente):
        self.numero = randint(1000000000000000,9999999999999999)
        self.titular=titular
        self.validade='{}/{}'.format(CartaoCredito._dataHora().month,CartaoCredito._dataHora().year+4)
        self.cod='{}{}{}'.format(randint(0,9),randint(0,9),randint(0,9))
        self.limite=None
        self.conta_corrente=conta_corrente
        conta_corrente.cartoes.append(self)
        


contaKiw=ContaCorrente("kiw","12345",333,444)

cartaokiw =CartaoCredito('kiwsley',contaKiw)

print(cartaokiw.titular)

print(cartaokiw.conta_corrente.numConta)

print(cartaokiw.numero)
print(cartaokiw.cod)


print(cartaokiw.validade)