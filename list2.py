lista = []
for n in range(3):
    nota = int(input(f"Digite a nota do {n+1}° elemento da lista: "))
    lista.append(nota)
#Calcular a média das notas da lista.
maioresquemedia = []
media = sum(lista)/len(lista)
for nota in lista:
    if nota > media:
        maioresquemedia.append(nota)

print("Lista de notas maiores qur a média", maioresquemedia)