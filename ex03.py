numero = int (input('Digite um número: '))
fatorial = 1
if numero <0:
    print ('não existe fatorial de número negativo')

else:
    for i in range (1, numero +1):
        fatorial*=i

    print (fatorial)