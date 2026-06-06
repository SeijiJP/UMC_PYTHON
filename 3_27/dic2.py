#Elaborar um programa que cadastre cursos em um dicionário, no qual a chave seja o código do curso e o valor seja outro dicionário contendo:
#nome do curso, carga horária e quantidade de vagas.
#O programa deve permitir consultar os dados de um curso pelo código.

cursos = {}

qtd = int(input("Quantos cursos deseja cadastrar? "))

for i in range(qtd):
    codigo = input("Código do curso: ")

    cursos[codigo] = {
        "nome": input("Nome do curso: "),
        "carga_horaria": int(input("Carga horária: ")),
        "vagas": int(input("Quantidade de vagas: "))
    }

codigo_busca = input("\nDigite o código do curso para consulta: ")

if codigo_busca in cursos:
    print(cursos[codigo_busca])
else:
    print("Curso não encontrado.")