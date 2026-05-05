#print
"""
print(12, 34, 1110, sep="-")

#tipos de dados

str - string -> só texto
int -> número inteiro, sendo positivo ou negativo
float -> número com ponto(virgula)
bool -> boolean, só existe duas respostas, true or false

input -> recebe dados

#operadores lógicos

and -> (e) 
#ele vai parar aqui porque só pode ser True
print(True and False and True)

entrada = input("[E]ntrar, [S]air: ")
senha = input("Senha:")

senha_permitida = "1234"

if entrada == "E" and senha == senha_permitida:
    print("Entrar")
else:
    print("Sair")

or -> (ou)
(if entrada == "E" or "e") and senha == senha_permitida:
senha = true or false or 0 or "abc" or "sem senha"
print(senha)

not -> (não)

print(not True)# False
print(not False)# True
"""

"in" and "not in"

nome = input("Diga seu nome: ")
encontrar = input("Diga oque quer encontar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")

else:
    print(f"{encontrar} não está em {nome}")

    
