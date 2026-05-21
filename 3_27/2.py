# 2) Elaborar um algoritmo que o usuário deve inserir um valor para A e outro valor N.
# Caso N seja negativo ou ZERO ou menor que A, o programa deve solicitar outro valor para N (apenas N).
# Logo após, o programa deve exibir a soma dos números de A até N.
A = int(input("Digite um valor: "))
N = int(input("Digite mais um valor: "))

while N <= 0 or N < A:
    N = int(input("Digite outro valor, o anterior é invalido: "))

soma = 0

while A <= N:
    soma += A
    A += 1

print(f"A soma dos valores de A a N é {soma}")