valor_total = 0
valor_100 = 0
valor_101 = 0
valor_102 = 0
valor_103 = 0
valor_104 = 0
valor_105 = 0

codigo = int(input("Digite o código do produto(digite um número diferente de 100,101,102,103,104 e 105 para parar): "))
while codigo < 105 and codigo > 99:

  if codigo == 100:
    preco = 1.20
    quantidade = int(input("Digite quantos produtos: "))
    while quantidade < 0:
      print("Digite uma quantidade válida")
      quantidade = int(input("Digite quantos produtos: "))
    valor_100 += (preco*quantidade)
    valor_total += (preco*quantidade)
    codigo = int(input("Digite o código de outro produto(digite um número diferente de 100,101,102,103,104 e 105 para parar): "))


  if codigo == 101:
    preco = 1.30
    quantidade = int(input("Digite quantos produtos: "))
    while quantidade < 0:
      print("Digite uma quantidade válida")
      quantidade = int(input("Digite quantos produtos: "))
    valor_101 += (preco*quantidade)
    valor_total += (preco*quantidade)
    codigo = int(input("Digite o código de outro produto(digite um número diferente de 100,101,102,103,104 e 105 para parar): "))

  if codigo == 102:
    preco = 1.50
    quantidade = int(input("Digite quantos produtos: "))
    while quantidade < 0:
      print("Digite uma quantidade válida")
      quantidade = int(input("Digite quantos produtos: "))
    valor_102 += (preco*quantidade)
    valor_total += (preco*quantidade)
    codigo = int(input("Digite o código de outro produto(digite um número diferente de 100,101,102,103,104 e 105 para parar): "))

  if codigo == 103:
    preco = 1.20
    quantidade = int(input("Digite quantos produtos: "))
    while quantidade < 0:
      print("Digite uma quantidade válida")
      quantidade = int(input("Digite quantos produtos: "))
    valor_103 += (preco*quantidade)
    valor_total += (preco*quantidade)
    codigo = int(input("Digite o código de outro produto(digite um número diferente de 100,101,102,103,104 e 105 para parar): "))

  if codigo == 104:
    preco = 1.30
    quantidade = int(input("Digite quantos produtos: "))
    while quantidade < 0:
      print("Digite uma quantidade válida")
      quantidade = int(input("Digite quantos produtos: "))
    valor_104 += (preco*quantidade)
    valor_total += (preco*quantidade)
    codigo = int(input("Digite o código de outro produto(digite um número diferente de 100,101,102,103,104 e 105 para parar): "))

  if codigo == 105:
    preco = 1.00
    quantidade = int(input("Digite quantos produtos: "))
    while quantidade < 0:
      print("Digite uma quantidade válida")
      quantidade = int(input("Digite quantos produtos: "))
    valor_105 += (preco*quantidade)
    valor_total += (preco*quantidade)
    codigo = int(input("Digite o código de outro produto(digite um número diferente de 100,101,102,103,104 e 105 para parar): "))

print("O valor a ser pago de cachorro quente é: {:.2f}".format(valor_100))
print("O valor a ser pago de bauru simples é: {:.2f}".format(valor_101))
print("O valor a ser pago de bauru com ovo é: {:.2f}".format(valor_102))
print("O valor a ser pago de hambúguer é: {:.2f}".format(valor_103))
print("O valor a ser pago de cheeseburguer é: {:.2f}".format(valor_104))
print("O valor a ser pago de refrigerante é: {:.2f}".format(valor_105))
print("O valor a ser pago total é: {:.2f}".format(valor_total))