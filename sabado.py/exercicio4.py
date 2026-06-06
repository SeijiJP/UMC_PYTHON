#Crie uma lista com 16 números reais informados pelo usuário.

#Depois solicite duas posições válidas da lista e exiba a soma dos elementos dessas posições.

lista = []
for x in range(5):
    x = int(input("Digite um número: "))
    lista.append(x)

pos1 = int(input("Digite a primeira posição: "))
pos2 = int(input("Digite a segunda posição: "))

print(lista[pos1])
print(lista[pos2])