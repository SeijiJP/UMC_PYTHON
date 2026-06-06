#Crie um programa que leia vários números e pare quando o usuário digitar 0. Ao final exiba a soma de todos os números digitados.
soma = 0
numero = 1

while numero != 0:
    numero = int(input("Digite um número: "))

    if numero != 0:
        soma += numero

print(f"A soma dos números digitados é {soma}")