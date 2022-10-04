divida = float(input("Digite o valor da dívida: "))
parcelas = 1

print("VALOR DA DIVIDA     VALOR DOS JUROS     QUANTIDADE DE PARCELAS    VALOR DA PARCELA ")
while parcelas <= 6:
    if parcelas == 1:
        juros = 0
    else:
        if parcelas == 3:
            juros = 10
        else:
            juros = 15

    valor_juros = divida * (juros / 100)
    valor_divida = divida * ((juros / 100) + 1)
    valor_parcela = valor_divida / parcelas

    print("     R$ ", valor_divida, "        R$ ", valor_juros, "                 ", parcelas,
          "              R$  {:.2f}".format(valor_parcela))

    if parcelas == 1:
        parcelas -= 1
    parcelas += 3