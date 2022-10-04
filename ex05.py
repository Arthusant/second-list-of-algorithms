numero = int (input('informe a quantidade de quadriláteros: '))
if numero <=0:
    print ('por favor digite um valor maior que 0!')

else:
    for i in range (numero):
        lado = float(input(f'informe o lado quadrilátero {i + 1}: '))
        print(f'Aréa: {lado * lado}')