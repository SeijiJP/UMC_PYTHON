# 1) Elaborar um algoritmo que leia um número inteiro positivo N (validar o número positivo)
# e deve exibir todos os números de 0 até N em ordem decrescente.
num = int(input("Digite um número positivo: "))

while num < 0:
    num = int(input("Número invalido, Digite novamente: "))
while num >= 0:
    print(num)
    num -= 1