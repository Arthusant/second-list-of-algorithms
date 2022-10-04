quant_num = 0
soma_par = 0
quant_par = 0
quant_impar = 0
soma_geral = 0

numero = int(input("Digite um numero: "))
while numero < 0:  # zero é par mas não é positivo por isso ele não entra na variavel de numeros pares
  print("Digite um número válido")
  numero = int(input("Digite um numero: "))

while numero != 0:
  if numero % 2 == 0:
    if numero == 0:
      soma_par -= 1 # -1 pois quando feito o calculo de 0 % 2 0 é par e não queremos que 0 indique nenhum numero2
    else:
      soma_par += numero
      quant_par += 1
      quant_num += 1
      soma_geral += numero
      numero = int(input("Digite um numero: "))
      while numero < 0:
        print("Digite um número válido")
        numero = int(input("Digite um numero: "))
  else:
    quant_impar += 1
    quant_num += 1
    soma_geral += numero
    numero = int(input("Digite um numero: "))
    while numero < 0:
      print("Digite um número válido")
      numero = int(input("Digite um numero: "))


media_par = soma_par / quant_par
media_geral = soma_geral / quant_num

print("A quantidade de numeros pares é: ", quant_par)
print("A quantidade de numeros impares é: ", quant_impar)
print(quant_num)
print("A média dos numeros pares: {:.2f}".format(media_par))
print("A média geral foi de: {:.2f}".format(media_geral))