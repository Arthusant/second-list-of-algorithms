cont = 0
resposta = "S"
mais_Antigo = mais_Novo = 0
meses = []

while resposta == "S":

    resposta = input("Deseja adicionar um empregado[S/N]: ").upper()

    while resposta not in "SN":
        resposta = input("Deseja adicionar um empregado[S/N]: ").upper()

    cont += 1

    if resposta == "S":
        numero_empregado = input("Número do empregado: ")
        numero_meses = input("Número de meses na empresa: ")

        while numero_meses in meses:
            numero_meses = input("Inválido, nesse mês já houve contratação, tente novamente: ")

        meses.append(numero_meses)

        if cont == 1:
            mais_Antigo = maisNovo = numero_empregado

        if numero_meses > mais_Antigo:
            mais_Antigo = numero_empregado

        if numero_meses < maisNovo:
            mais_Novo = numero_empregado

    elif resposta == "N":
        print(f"Funcionário mais antigo: {mais_Antigo}")
        print(f"Funcionário mais novo: {mais_Novo}")