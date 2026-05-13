lista = []
for x in range(10):
    valor = int(input(f"Digite o {x+1}°valor da lista."))
    lista.append(valor)

continuar = "s"
while continuar == "s":

    p = int(input("Digite o valor que deseja procurar: "))
    if p in lista:
        posicao = lista.index(p)
        print("Valor encontrada")
        print(f"Posição: {posicao}")
    else:
        print("Valor não existente")
continuar = input("deseja continuar a busca? (s/n): ").lower()
print("programa encerrado")