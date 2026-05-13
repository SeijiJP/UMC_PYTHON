lista = []
while len(lista) < 20:
    numero = int(input("Digite um número inteiro maior ou igual a 40: "))
    if numero < 40:
        print("Número invalido. Digite um número maior ou igual a 40")
    elif numero in lista:
        print("Este número ja existe na lista. Digite um número diferente.")
    else:
        lista.append(numero)
        print("Lista final", lista)
aa