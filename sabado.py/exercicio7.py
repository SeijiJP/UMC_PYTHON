#Crie um sistema simples de estoque utilizando duas listas:

#* nomes dos produtos
#* quantidade dos produtos

#Classifique:

#* Estoque crítico (< 5)
#* Estoque baixo (5 a 10)
#* Estoque normal (>10)

nomes = []
quantidades = []
criticos = []

for x in range(5):
    nome = str(input("Digite o nome do produto: "))
    quantidade = int(input("Digite a quantidade de produtos: "))
    nomes.append(nome)
    quantidades.append(quantidade)

    if quantidade < 5:
        situacao = ("estoque critico")
        criticos.append(nome)
    elif 5 <= quantidade <=10:
        situacao = ("Estoque baixo")
    else:
        situacao = ("Estoque normal")
    
    print(nome, " ", situacao)
