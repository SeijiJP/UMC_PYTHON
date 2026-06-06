#Crie um programa que leia 20 números inteiros, armazene-os em uma lista e exiba:

#* o maior valor
#* o menor valor
lista = []
for i in range (5):
    i = int(input("Digite um número: "))
    lista.append(i)

maior = max(lista)
print(f"maior numero da lista é {maior}")
menor = min(lista)
print(f"o menor numero da lista é {menor}")
diferenca = maior - menor
print(f"a diferença do {maior} para o {menor} é de {diferenca}")