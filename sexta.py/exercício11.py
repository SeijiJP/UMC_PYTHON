#Crie um programa que solicite uma senha e continue pedindo até que o usuário digite a senha correta.

senha_correta = "1234"
senha = int(input("Digite a sua senha: "))

while senha != senha_correta:
    print("senha incorreta")
    senha = input("Digite a senha correta: ")
print("acesso liberado")