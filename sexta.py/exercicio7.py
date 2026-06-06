#Crie um programa que leia dois números inteiros A e N.

#N deve ser maior que A e diferente de zero.

#Caso contrário, solicite um novo valor para N.

#Ao final exiba a soma de todos os números entre A e N.

A = int(input("Digite um número: "))
N = int(input("Digite mais um número: "))

while N <= A or N==0:
    N = int(input("Digite um número que seja maior que o primeiro número digitado: "))

soma = 0

for i in range(A, N+1):

    soma +=i

print(soma)



