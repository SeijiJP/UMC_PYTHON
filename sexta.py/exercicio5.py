#Crie um programa que leia um número e informe se ele é:

# positivo
# negativo
# igual a zero

numero = int(input("Digite um número: "))

if numero >=1:
    resultado = "positivo"
elif numero <= -1:
    resultado = "negativo"
else:
    numero ==0
    resultado = "zero"

print(f"seu número é {resultado}")