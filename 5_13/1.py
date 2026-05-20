def verificar(palavra):
    invertida = palavra[::-1]
    if palavra == invertida:
        print("É um palindromo")
    else:
        print("Não é um palindromo")
texto = input("Digite um palavra: ")
verificar(texto)
#AAAA