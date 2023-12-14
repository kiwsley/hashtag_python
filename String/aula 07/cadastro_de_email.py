nome=input('digite seu nome:')
email= input('digite seu e-mail:')

if nome and email:
    pos_a=email.find('@')
    servidor = email[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print ('cadastro concluido')
    else:
        print ('email invalido')
else:
    print('digite seu nome corretamente')