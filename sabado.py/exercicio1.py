#Crie um programa que leia 6 números inteiros e os armazene em uma lista. Depois exiba cada número juntamente com sua posição na lista.
lista = []
for i in range(1,6):
    n = int(input("Digite um número: "))
    lista.append(n)

for i in range(1, 6):
        print(f"Posição {i}: {lista[i]}")



