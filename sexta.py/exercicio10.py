#Crie um programa que solicite um número e exiba sua tabuada de 1 até 10

n = int(input("Digite um número: "))

for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")