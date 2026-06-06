#Crie um programa que leia duas notas (P1 e P2) e calcule:

#Media = (P1 + P2 * 2) / 3

#Resultado:

#* Média >= 5 → APROVADO
#* Média >= 3 e < 5 → EXAME
#* Média < 3 → REPROVADO

#Se estiver de EXAME, solicite a nota do exame e calcule:

#MF = (Media + Exame) / 2

#Informe se o aluno foi aprovado ou reprovado.

p1 = int(input("Digite a nota da prova: "))
while p1 <0 or p1 >10:
    p1 = int(input("Digite uma nota real: "))

p2 = int(input("Digite o nota da outra prova: "))
while p2 <0 or p2 >10:
    p2 = int(input("Digite uma nota real"))

media = (p1 + p2 *2)/3

if media >= 5:
    print("Aprovado")
elif media <5 or media >3:
    print("exame")
    exame = int(input("Digite a nota do exame: "))
    mf = (exame + media) / 2 
    if mf >5:
        print("aprovado")
    else:
        print("reprovado")
else:
    media <3
    print("reprovado")