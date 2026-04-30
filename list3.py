lista_A = []
for n in range(3):
    valores = int(input(f"Digite o {n+1}° número da lista: "))
    lista_A.append(valores)

lista_B = []

for n in lista_A:
    if n % 2 == 0:
        lista_B.append(valores ** 2)
    else:
        lista_B.append(valores ** 3)

lista_B.sort()
print("Nova lista ordenada", lista_B)