n = int (input('Informe com quantos termos a serie será realizada: '))
if n <=0:
    print ('Não é possivel realizar uma quantidade de termos negativos')
else:
    count = 0
    soma = 0
    for i in range (1,n+1,2):
        count +=1
        soma += count/i
    print (f'A soma dos da série é {soma}')