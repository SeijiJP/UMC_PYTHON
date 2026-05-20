#Elaborar um programa em que o usuário deva preencher uma lista com 30 números.
#Após o preenchimento o programa deve calcular a média dos números inseridos. 
#Logo em seguida, o programa deve salvar em outra lista somente os números que são maiores que a média. 
#Exibir no final a lista dos números maiores que a média.

lista1= []
maior= []
for i in range(30):
    valor = int(input(f'Digite o {i+1}° valor da lista: '))
    lista1.append(valor)
media = sum (lista1) / len (lista1)
for valor in lista1:
    if valor > media:
        maior.append(valor)

print(f"Media dos números: {media} ")

print("maiores que a média: ")
print(maior)
        