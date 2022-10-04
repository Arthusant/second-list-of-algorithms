verifica = 1
sequencia = 0

numero = int(input('Informe o valor e verifique se pode ser um número triangular: '))

while verifica == 1:
    sequencia += 1
    for a in range(1, sequencia + 1):
        pass
    for b in range(1, sequencia + 2):
        pass
    for c in range(1, sequencia + 3):
        pass

    if (a * b * c) == numero:
        print(f'É trinagular pois: {numero} = {a} * {b} * {c}')
        verifica = 0
    else:
        if (a * b * c) > numero:
            print('Não é trinagular.')
            verifica = 0