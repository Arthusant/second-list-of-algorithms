count = 0
soma = 0
for i in range (1000,0, -3):
    if count == 50:
        break
    count += 1
    soma += i/count
print (f'A soma dos 50 primeiros termos é: {soma}')