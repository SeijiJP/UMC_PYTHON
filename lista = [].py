lista = []
#Digitando os números da lista.
for x in range(5):
    valor = int(input(f"Digite o valor do {x+1}° número da lista: "))
    lista.append(valor)
#Digitar a posição do número da lista
p1 = int(input("Digite a posição dos múmeros da lista: "))
while p1 <0 or p1 >16:
    print("Posição invalido")
    p1 = int(input("Digite outro número novamente>"))

#Digitar a posição do número da lista
p2 = int(input("Digite a posição dos múmeros da lista: "))
while p2 <0 or p2 >16:
    print("Posição inválida")
    p2 = int(input("Digite outro número novamente"))
#Somando a p1 com a p2
soma = lista[p1] + lista[p2]
print(f"A soma dos resultados foi {soma}")