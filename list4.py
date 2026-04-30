nomes = []
quantidade = []
#entrada de dados
for i in range(4):
    nome = input(f"Digite o nome do {i+1}° produto: ")
    qtd = int(input(f"Digite a quantidade de {nome} em estoque: "))
    nomes.append(nome)
    quantidade.append(qtd)

    estoque = []

for i in range(len(nomes)):
    if quantidade[i] <5:
        classificacao = "Estoque crítico!!"
    elif 5 <=quantidade[i] <=10:
        classificacao = "Estoque baixo!"
    else:
        classificacao = "Estoque normal"

print(f"{nomes[i]}: {classificacao}")

print("Produtos com estoque crítico")
print(estoque)