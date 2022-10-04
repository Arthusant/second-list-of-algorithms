valor_x = int(input('Informe o valor de X: '))
if valor_x <0:
    print ('não é possivel realizar a operação com um valor negativo, digite um positivo')
else:
    valor_y = 0
    for i in range (1,101):
        valor_y = (valor_x+i) + valor_y
    print(valor_y)