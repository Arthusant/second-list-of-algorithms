numero = int(input('Informe o numero de vezes que você quer somar: '))
if numero <0:
    print('Não é possivel realizar a operação, por favor digite um número positivo')

else:
    h = 0
    for i in range (1,numero +1):
        h+= 1/i
    print (f'O resultado será {h}')