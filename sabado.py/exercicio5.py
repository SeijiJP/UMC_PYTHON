#Crie um programa que leia 10 números.

#Calcule a média dos números.

#Crie uma nova lista contendo apenas os números maiores que a média.

#Exiba essa nova lista.

lista = []
lista2 = []

for n in range(5):
    n = int(input("Digite a nota: "))
    lista.append(n)
soma = 0
for nota in lista:
    soma += nota
media = soma / 5
print(media)

for nota in lista:

    if nota >= media:
        lista2.append(nota)
        print(f"As notas maiores que a media foram {nota}")

