
import ContasBancos

contaKiw=ContasBancos.ContaCorrente("kiw","12345",333,444)

cartaokiw =ContasBancos.CartaoCredito('kiwsley',contaKiw)

cartaokiw.senha ='2345'
print(cartaokiw.senha)

#print(contaKiw.__dict__)