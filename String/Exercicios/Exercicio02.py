''''
2. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, 
e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. 
O usuário pode informar o número com ou sem o traço separador.
'''

numero_telefone = input('Digite seu numero de telefone: ')

numero_telefone = numero_telefone.replace('-', '')

if len(numero_telefone) == 7:
    numero_telefone = '3' + numero_telefone
    print("Numero de telefone ajustado: {}".format(numero_telefone))
else:
     print("Numero não tem 7 digitos")

