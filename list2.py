lista = []
for x in range (3):
    nota = float(input(f"Digite a {x+1}° nota: "))
    lista.append(nota)

maioresqueamedia = []
media = sum(lista) / len(lista)
for nota in lista:
    if nota > media:
        maioresqueamedia.append(nota)

print("Lista de notas maiores que a média: ", maioresqueamedia)