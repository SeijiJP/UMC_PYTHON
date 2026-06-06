#Crie um programa que leia 15 números inteiros.

#Crie uma nova lista:

#* se o número for par, armazene o quadrado
#* se for ímpar, armazene o cubo

lista = []
par = []
impar = []

for i in range(5):
    x = int(input("Digite o número: "))
    lista.append(x)

for x in lista:
    if x % 2 ==0:
        resultado = x**2
        par.append(resultado)
    else:
        resultado = x**3
        impar.append(resultado)
        
print("Lista original",lista)   
print("Pares ao quadrado",par)
print("impares ao cubo",impar)