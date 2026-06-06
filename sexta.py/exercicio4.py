#Crie um programa que receba a idade de um atleta e o classifique:

#5 a 10 anos: Infantil
#11 a 15 anos: Juvenil
#16 a 20 anos: Júnior
 # #21 a 25 anos: Profissional

idade = int(input("Digite sua idade: "))

if idade >= 5 and idade <=10:
    resultado = "Infantil"
elif idade >=11 and idade <= 15:
    resultado = "Juvenil"
elif idade >= 16 and idade <=20:
    resultado = "Junior"
elif  idade >= 21 and idade <=25:
     resultado = "Profissional"
else:
    resultado = "Fora das categorias"
    
print(f"Com sua idade voce ira participar do time {resultado}")

    