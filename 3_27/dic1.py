#Elaborar um programa que registre em um dicionário o nome de vários setores de uma empresa como chave e a quantidade
#de funcionários em cada setor como valor (o usuário deve inserir os dados).
#O programa deve identificar e exibir o setor com o maior número de funcionários.

setores = {}

qtd = int(input("Quantos setores deseja cadastrar? "))

for i in range(qtd):
    nome = input("Nome do setor: ")
    funcionarios = int(input("Quantidade de funcionários: "))
    setores[nome] = funcionarios

maior_setor = max(setores, key=setores.get)

print(f"\nSetor com mais funcionários: {maior_setor}")
print(f"Quantidade: {setores[maior_setor]}")

