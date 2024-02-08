import string
from collections import Counter

def analisar_texto(texto):
    """"
    Analisa o texto fornecido e calcula a contagem de palavras, a frequencia de palavras e frequencia de letras.

    retorna 

    uma tupla analisada
    """
    texto_tratado = texto.translate(str.maketrans("","",string.punctuation))
    palavras = texto_tratado.split()
    contagem_palavras = len(palavras)
    frequencia_palavras = Counter(palavras)
    frequencia_letras = Counter(texto_tratado.lower())

    return contagem_palavras,frequencia_palavras,frequencia_letras

texto = input("digite seu texto para a contagem: ")

contagem_palavras,frequencia_palavras,frequencia_letras = analisar_texto(texto) 

print(f"contagem de palavras: {contagem_palavras}")
print(f"frequencia de palavras: {frequencia_palavras}")
print(f"frequencia de letras: {frequencia_letras}")

