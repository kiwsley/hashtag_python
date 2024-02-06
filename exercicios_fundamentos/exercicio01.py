faturamento = {
    'jan': 'R$ 95.141,98',
    'fev': 'R$ 95.425,16',
    'mar': 'R$ 89.716,31',
    'abr': 'R$ 78.459,99',
    'mai': 'R$ 71.087,28',
    'jun': 'R$ 83.911,06',
    'jul': 'R$ 56.467,26',
    'ago': 'R$ 88.513,58',
    'set': 'R$ 66.552,49',
    'out': 'R$ 80.164,07',
    'nov': 'R$ 66.964,33',
    'dez': 'R$ 71.525,25',
}

# Percorrer cada item do dicionario

#para cada mês eu vou: 
    #transformar o valor em numero
    # calcular o importo mensal
    #calcular o imposto trimestral
    #construir o resultado

def transformar_numero(valor):
    valor = valor.replace("R$ ", "")
    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")
    valor = float(valor)
    return valor 
def calcular_imposto_mensal(valor):
    iss = 0.05* valor
    pis = 0.0065* valor
    cofins = 0.03 * valor
    imposto_mensal = iss+pis+cofins
    return imposto_mensal

def calcular_imposto_trimestral(valor):
    ir = 0.048 * valor
    csll = 0.0288 * valor
    if valor > 20000:
        ir_adicional = (valor - 20000) * 0.1
    else:
        ir_adicional = 0

    imposto_trimestral =ir + csll+ ir_adicional
    return imposto_trimestral


for mes in faturamento:
   valor = transformar_numero(faturamento[mes])
   imposto_mensal = calcular_imposto_mensal(valor)
   imposto_trimestral = calcular_imposto_trimestral(valor)
   

   faturamento[mes] = (valor, imposto_mensal, imposto_trimestral)

print (faturamento, sep='\n')