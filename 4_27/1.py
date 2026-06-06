#1) Elaborar um programa que contenha uma lista com 16 elementos
#  em que o usuário deve preencher com valores reais. Logo em seguida,
#  deve ser solicitado ao usuário que digite dois números. Esses números devem corresponder a posições na lista (caso contrário solicite um novo valor).
#  Após inserir os dois números o programa deve exibir a soma dos elementos das duas posições da lista.
lista = []

for i in range(1,17 ):
    valor = int(input(f"Digite o valor da posição {i}: "))
    lista.append(valor)

p1 = int(input("Digite a primeira posição (0 a 15): "))
while p1 < 0 or p1 > 15:
    p1=int(input("Posição invalida. Digite novamente: "))
p2 = int(input("Digite a segunda posição (0 a 15)"))
while p2 < 0 or p2 > 15:
    p2= int(input("Posição invalida. Digite novamente: "))

soma = lista [p1] + lista [p2]
print(f'Soma dos elementos: {soma}')
