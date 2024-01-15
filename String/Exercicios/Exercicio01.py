''''
1. Tamanho de strings. Faça um programa que leia 2 
strings e informe o conteúdo delas seguido do seu comprimento.
 Informe também se as duas strings possuem o mesmo comprimento e 
 são iguais ou diferentes no conteúdo.
'''


string_1 = input("Digite a frase 1 : ")
string_2 = input("Digite a frase 2 : ")

print("O tamanho da frase  1 é de {} Caracteres".format(len(string_1)))
print("O tamanho da frase  2 é de {} Caracteres".format(len(string_2)))

if string_1==string_2:
    print("Tem o mesmo conteúdo")
else:
    print("conteúdo diferente")

if len(string_1) == len(string_2):
    print("O tamanho das strings são iguais")
else:
    print("O tamanho das strings são diferentes")