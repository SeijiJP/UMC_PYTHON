#Crie um programa que leia o salário e o cargo de um funcionário.

#Considere:

#* Gerente: aumento de 10%
#* Engenheiro: aumento de 20%
#* Técnico: aumento de 30%
#* Outros cargos: aumento de 40%

cargo = input("Digite seu cargo atual: ")
salario = int(input("Digite seu salario atual: "))

if cargo == "gerente":
    aumento = salario * 1.10
elif cargo == "engenheiro":
    aumento = salario * 1.20
elif cargo == "tecnico":
    aumento = salario * 1.30
else:
    aumento = salario * 1.40

print(f"Seu salário com o aumento é de {aumento:.2f}")
print(f"Seu salário antigo era de {salario}")
print(f"A diferença de salarios deles é de {aumento - salario}")