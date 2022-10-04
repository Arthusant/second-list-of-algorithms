numero1 = int (input('Digite um valor inteiro: '))
if numero1 <0:
    print('por favor, digite um valor válido')
else:
    numero2 = int (input('Digite o segundo valor: '))
    if numero2 <0:
        print ('Por favor digite um número positivo!')
    else:
        if numero1 == numero2 or numero2 == numero1+1:
            print ('Para os números apresentados não há intervalo')
        else:
            print (f'Os numeros do intervalo entre {numero1} e {numero2} são: ')
            for n in range (numero1+1,numero2):
                print (n,end = ' ')