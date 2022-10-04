valor_A = int(input('Digite o valor de A: '))
valor_B = int(input('Digite o valor de B: '))
total = 1
if valor_B < 0:
    for i in range (abs(valor_B)):
        total *= (1/valor_A)
for n in range (valor_B):
    total *= valor_A
print (f'O expoente do valor {valor_A} é {total}')