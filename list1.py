lista = []
#colocando os números reais aqui dentro
for x in range (16):
    valor = float(input(f"Digite o {x+1}° número: ")) 
    lista.append(valor)

p1 =int(input("Digite o valor da primeira posição: "))
while p1 < 0 or p1 > 15:
    print("Posição invalida")
    p1 =int(input("DIgite novamente: "))

p2 = int(input("Digite o valor da segunda posição do número:"))
while p2 <0 or p2 > 15:
    print("Posição invalida")
    p2 = int(input("Digite novamente: " ))

soma = lista[p1] + lista[p2]

print(f"Soma:{soma}")