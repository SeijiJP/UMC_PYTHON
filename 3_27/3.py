# 3) Elaborar um algoritmo que lê duas notas (P1 e P2) e calcule a média [Media=(P1+P2*2)/3].
# Caso a média seja maior igual a 5 deve exibir a mensagem “APROVADO”.
# Caso a média seja menor que 5 e maior igual a 3 deve exibir a mensagem “EXAME”.
# Caso contrário exibir a mensagem “REPROVADO”.
# Caso esteja de exame o programa deve solicitar a nota de exame e verificar se o aluno está aprovado ou não [MF=(Media+EXAME)/2].
# Caso a média final seja maior igual a 5 deve exibir a mensagem “APROVADO”.
# Caso a média final seja menor que 5 deve exibir a mensagem “REPROVADO”.
# Só deve aceitar notas entre 0 e 10.
# No final do programa exibir a mensagem: "Deseja continuar? (s/n)".
# Se digitar “s” deve repetir, caso contrário termina.
p1 = float (input("Digite a nota da primeira nota: "))
while p1 < 0 or p1 >10:
    p1 = float(input("Nota invalida"))
p2 = float (input("Digite a nota da segunda nota: "))
while p2 < 0 or p1 >10:
    p2 = float(input("Nota invalida"))

media = (p1 + p2*2)/3

if media > 5:
    print("aprovado")
elif media < 5 and media > 3:
    print("exame")
    
    exame = int(input("Digite a nota do exame: "))
    while exame < 0 or exame > 10:
        print("Nota invalida")
    
    mf = (media + exame) / 2

    if mf > 5:
        print("aprovado")
    else:
        print("reprovado")
else:
    print("reprovado")

continuar = input("Deseja continuar? sim ou não: " ).lower()
