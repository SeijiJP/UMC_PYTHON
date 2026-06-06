#Crie um programa que leia um número inteiro positivo N.
#Caso o número seja inválido, solicite novamente.
#Depois exiba todos os números de N até 0 em ordem decrescente.

N = int(input("Digite um número positivo: "))

for i in range(N, -1, -1):
    print(i)

