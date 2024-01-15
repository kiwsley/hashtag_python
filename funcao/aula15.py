def descobrir_servidor(email):
    try:
        posicao_a = email.index('@')
    except:
        raise ValueError("NÃO TEM O @")
    else:
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            return'gmail'
        elif 'hotmail' in servidor:
            return'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        else:
            return"não determinado"
   

print(descobrir_servidor('teste'))