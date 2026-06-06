#Elaborar um programa que armazene em um dicionário o nome de 5 supermercados
#como chave e uma lista contendo os faturamentos dos últimos 4 meses como valor.
#O programa deve calcular a média de faturamento de cada supermercado.

supermercados = {}

for i in range(5):
    nome = input(f"\nNome do supermercado {i+1}: ")

    faturamentos = []
    for j in range(4):
        valor = float(input(f"Faturamento do mês {j+1}: "))
        faturamentos.append(valor)

    supermercados[nome] = faturamentos

for nome, valores in supermercados.items():
    media = sum(valores) / len(valores)
    print(f"{nome}: R$ {media:.2f}")