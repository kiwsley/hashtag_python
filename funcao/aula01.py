

def cadastrar_produto():
    produto = input("digite o nome do produto que deseja cadastrar: ")
    produto = produto.casefold()
    produto = produto.strip()
    return produto

produto=cadastrar_produto()

print (produto)