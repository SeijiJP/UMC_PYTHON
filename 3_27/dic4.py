#Elaborar um programa que cadastre equipamentos de informática em um dicionário,
#no qual a chave seja o número de patrimônio e o valor seja outro dicionário contendo: descrição, setor e estado de conservação.
#O programa deve permitir listar todos os equipamentos cadastrados

equipamentos = {}

qtd = int(input("Quantos equipamentos deseja cadastrar? "))

for i in range(qtd):
    patrimonio = input("Número de patrimônio: ")

    equipamentos[patrimonio] = {
        "descricao": input("Descrição: "),
        "setor": input("Setor: "),
        "estado": input("Estado de conservação: ")
    }

for patrimonio, dados in equipamentos.items():
    print(f"\nPatrimônio: {patrimonio}")
    print(f"Descrição: {dados['descricao']}")
    print(f"Setor: {dados['setor']}")
    print(f"Estado: {dados['estado']}")