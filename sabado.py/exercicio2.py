#Crie um programa que leia 4 números reais, armazene-os em uma lista e exiba:

#* as notas digitadas
#* a média das notas

lista = []
for i in range(4):
    n = int(input("Digite sua nota: "))
    lista.append(n)

for i in range(4):
    print(f"As notas são: {lista [i]}")

soma = 0
for nota in lista:
    soma += nota
media = soma / 4
print(f"A media das notas são {media}")

