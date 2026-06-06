#Crie um programa que leia uma letra digitada pelo usuário e informe se ela é uma vogal ou uma consoante. Caso não seja uma letra válida, exiba uma mensagem de erro.

letra = str(input("Digite uma letra: "))

if letra in "aeiou":
    resultado = "vogal"
elif letra.isalpha():
    resultado = "consoante"
else:
    resultado = "erro"
print(f"Sua letra é uma {resultado}.")