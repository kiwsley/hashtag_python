import string
import random

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

print(random.choice(string.digits))

escolhas=random.choices(string.digits,k=3)
print(escolhas)
random.shuffle(escolhas)
print(escolhas)

def gerar_senha(tamanho):
    if tamanho < 4:
        print("O tamanho da senha precisa ser no minimo 4 caracteres")

    else: 
        senha = [
            random.choice(string.ascii_letters),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        possibilidades="".join([string.ascii_letters,string.digits,string.punctuation])
        senha.extend(random.choices(possibilidades, k = tamanho -3))
        random.shuffle(senha)

        return "".join(senha)

tamanho = int( input("Digite o comprimento da senha: "))
print(gerar_senha(tamanho))