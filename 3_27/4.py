# 4) Elaborar um algoritmo para um caixa de uma lanchonete.
# Este algoritmo a cada item inserido deve ler o código do item (validar o código, caso contrário solicitar um código válido).
# Logo em seguida, sempre deve exibir a mensagem: “Adicionar novo item? (s/n)”.
# Sempre que digitar “s”, o usuário deve continuar inserindo um novo item.
# O algoritmo termina, caso digite “n” e deve apresentar o valor total a ser pago.
# O cardápio da lanchonete deve estar neste arquivo como parte da descrição.
# Cardápio:
# Código  Descrição do item  Preço
# 100     Cachorro quente    R$ 3,50
# 101     Bauru simples      R$ 3,80
# 102     Bauru com ovo      R$ 4,50
# 103     Hambúrguer         R$ 4,70
# 104     Cheeseburguer      R$ 5,30
# 105     Refrigerante       R$ 4,00

produto = int(input("Digite o código do produto escolhido: "))
add = input("deseja por mais algum produto no carrinho? (s ou n)").lower()
