numero = int (input ('Digite um número para verificar se o mesmo é primo: '))
total = 0
for i in range (1,numero+1):
    if numero % i == 0:
        total += 1
print (f'O número {numero} foi divisivel {total} vezes')
if total == 2:
    print (f'Por isso ele é primo!')
else:
    print ('Por isso ele não é primo!')
