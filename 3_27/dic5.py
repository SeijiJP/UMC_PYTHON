#Elaborar um programa que cadastre filmes em um dicionário,
#no qual a chave seja um código identificador e o valor seja outro dicionário contendo: título,
#gênero e duração em minutos. O programa deve permitir listar apenas os filmes com duração superior a 120 minutos.

filmes = {}

qtd = int(input("Quantos filmes deseja cadastrar? "))

for i in range(qtd):
    codigo = input("Código do filme: ")

    filmes[codigo] = {
        "titulo": input("Título: "),
        "genero": input("Gênero: "),
        "duracao": int(input("Duração em minutos: "))
    }

print("\nFilmes com duração superior a 120 minutos:")

for codigo, dados in filmes.items():
    if dados["duracao"] > 120:
        print(f"{dados['titulo']} - {dados['duracao']} min")