#Crie um programa em Python que funcione como uma calculadora.
#O usuário deve informar dois números e escolher uma operação (+, -, * ou /).
#O programa deve exibir o resultado da operação escolhida.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite mais um número: "))
op = input("Digite uma das 4 operações matemáticas(+,-,/,*): ")

if op == "+":
    resultado = n1 + n2
elif op == "-":
    resultado = n1 - n2
elif op == "/":
    resultado = n1 / n2
elif op == "*":
    resultado = n1 * n2
    
print(f"o resultado da sua conta é: {resultado}")


    