import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='kiwsley',
    database='teste',
)

cursor = conexao.cursor()
#CRUD
nome_produto ="Todynho"
valor = 3
comando=f'INSERT INTO new_table (nome_produto, valor) VALUES ("{nome_produto}",{valor})'
cursor.execute(comando)
conexao.commit()
resultado = cursor.fetchall()





cursor.close()
conexao.close()