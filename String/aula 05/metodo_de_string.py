#capitalize() -> cola a 1° letra como maiuscula

texto = 'kiw'
print(texto.capitalize())

#casefold() -> transfoma tudo em minuscula
texto='KiW'
print (texto.casefold())

#count -> qunatidade de vezes que um valor aparece na string

texto = 'kiwsleyfreire@gmail.com.'
print(texto.count('.'))

#endswith() verifica se o texto termina com um valot especifo e dá uma resposta

print(texto.endswith('gmail.com.'))

# find() procura um texto dentro de outro texto e dar a posição

print(texto.find('@'))


#isalnum() verifica se há caracteres alfanumericos
#isalpha() cerifica se um texto é todo feito de letras
#isnumeric() verifica se um texto é todo feito de letras
#replace() substitui um tempo por outro em uma string
#split() separa uma string de acordo com um delimitador em varios textos diferentes
#splitlines() separa um texto em varios textos de acordo com os enters do texto
#upper() coloca o texto em maiusculo
#strip() retira caracteres indesejados dos texto, retira espaço extras no inicio e no final
#title() coloca 1° letra do titulo em maiscula
